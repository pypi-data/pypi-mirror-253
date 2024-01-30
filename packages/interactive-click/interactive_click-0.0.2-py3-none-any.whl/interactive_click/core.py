from copy import deepcopy
import os
import sys
from typing import Any, Callable, Sequence

import click
import questionary
from click.core import Context
from prompt_toolkit.document import Document

STYLES = {
    "help": "fg:#5f819d",
}


class ClickParameterValidatorAndConverter(questionary.Validator):
    def __init__(self, ctx: click.Context, param: click.Parameter) -> None:
        super().__init__()
        self.ctx = ctx
        self.param = param

    def convert(self, text: str):
        if not text:
            return self.param.default
        else:
            return text

    def validate(self, document: Document) -> None:
        try:
            text = document.text.strip()
            if self.param.required and not text:
                raise questionary.ValidationError(message="This is required")
            value = self.convert(text)
            self.param.process_value(self.ctx, value)
        except click.BadParameter as e:
            raise questionary.ValidationError(message=f"Invalid input: {e}") from e


class ClickPathParameterValidator(ClickParameterValidatorAndConverter):
    def convert(self, text: str):
        text = text.strip()
        if not text:
            return self.param.default
        else:
            return os.path.expanduser(text)


class ClickMultipleParametersValidator(ClickParameterValidatorAndConverter):
    def convert(self, text: str):
        return text.strip().split(",")


def ask_fn(*, unsafe: bool) -> Callable[[questionary.Question], Any]:
    return lambda q: q.unsafe_ask() if unsafe else q.ask()


def _make_questionary_choices(ctx: click.Context, choice_param: click.Parameter) -> list[questionary.Choice]:
    assert isinstance(choice_param.type, click.Choice)
    default = choice_param.default or set()
    assert default is None or hasattr(default, "__contains__")  # TODO: handle all cases
    choices = []
    for choice in choice_param.type.choices:
        is_selected = choice in default if hasattr(default, "__contains__") else choice == default  # type: ignore[operator]  # mypy doesn't like hasattr
        choices.append(questionary.Choice(title=choice, value=choice, checked=is_selected))
    return choices


def _ask_param(
    ctx: click.Context,
    param: click.Parameter,
    *,
    unsafe_ask: bool,
):
    assert param.name is not None
    name = param.human_readable_name
    type_name = param.type.name

    ask = ask_fn(unsafe=unsafe_ask)

    validator: questionary.Validator | None = None
    if isinstance(param.type, click.Path):
        validator = ClickPathParameterValidator(ctx, param)
        user_input = ask(
            questionary.path(
                f"Enter {name} ({type_name})",
                default=str(param.default) if param.default else "",
                validate=validator,
            )
        )
        if user_input is not None:
            user_input = validator.convert(user_input)

    elif param.type == click.BOOL:
        user_input = ask(
            questionary.confirm(
                f"{name} ({type_name})",
                default=param.default is True,
            )
        )

    elif isinstance(param.type, click.Choice) and not param.multiple:
        user_input = ask(
            questionary.select(
                f"Enter {name} ({type_name})",
                choices=_make_questionary_choices(ctx, param),
            )
        )

    elif isinstance(param.type, click.Choice) and param.multiple:
        user_input = ask(
            questionary.checkbox(
                f"Enter {name} ({type_name})",
                choices=_make_questionary_choices(ctx, param),
            )
        )

    elif param.multiple:
        validator = ClickMultipleParametersValidator(ctx, param)
        user_input = ask(
            questionary.text(
                f"Enter {name} ({type_name})",
                default=str(param.default) if param.default else "",
                validate=validator,
            )
        )
        if user_input is not None:
            user_input = validator.convert(user_input)
    else:
        validator = ClickParameterValidatorAndConverter(ctx, param)
        user_input = ask(
            questionary.text(
                f"Enter {name} ({type_name})",
                default=str(param.default) if param.default else "",
                validate=validator,
            )
        )
        if user_input is not None:
            user_input = validator.convert(user_input)

    return user_input


def _process_parameter(ctx: click.Context, param: click.Parameter, *, unsafe_ask: bool, show_help: bool):
    assert param.name is not None
    name = param.human_readable_name
    type_name = param.type.name

    if show_help and (help_text := getattr(param, "help", None)):
        msg = f"{name} ({type_name}): {help_text}"
        questionary.print(msg, style=STYLES["help"], end="\n")

    if param.nargs == -1:
        user_input = []
        while True:
            param_copy = deepcopy(param)
            param_copy.nargs = 1
            single_input = _ask_param(ctx, param_copy, unsafe_ask=unsafe_ask)
            if single_input is None:
                break
            user_input.append(single_input)
    elif isinstance(param.nargs, int) and param.nargs > 1:
        param_copy = deepcopy(param)
        param_copy.nargs = 1
        first_input = _ask_param(ctx, param_copy, unsafe_ask=unsafe_ask)
        if first_input is not None:
            user_input = [first_input]
            while len(user_input) < param.nargs:
                single_input = _ask_param(ctx, param_copy, unsafe_ask=unsafe_ask)
                if single_input is not None:
                    user_input.append(single_input)
        else:
            user_input = None
    else:
        user_input = _ask_param(ctx, param, unsafe_ask=unsafe_ask)

    param.handle_parse_result(ctx, {param.name: user_input}, [])


def _process_parameters(ctx: click.Context, params: Sequence[click.Parameter], *, unsafe_ask: bool, show_help: bool):
    for param in params:
        _process_parameter(ctx, param, unsafe_ask=unsafe_ask, show_help=show_help)


def _invoke_cmd(ctx: click.Context, cmd: click.Command):
    if cmd.callback is not None:
        return ctx.invoke(cmd.callback, **ctx.params)


def _run_interactive_multi(ctx: click.Context, cmd: click.MultiCommand, *, unsafe_ask: bool, show_help: bool):
    ask = ask_fn(unsafe=unsafe_ask)

    help_text = cmd.short_help or cmd.help or (f"Choose a command from {cmd.name}" if cmd.name else "Choose a command")
    if isinstance(cmd, click.Group):
        # Keep the commands in the same order they are defined in the group.
        commands = list(cmd.commands.keys())
    else:
        commands = cmd.list_commands(ctx)

    if show_help and cmd.help:
        questionary.print(cmd.help, style=STYLES["help"], end="\n")

    subcommand_user = ask(questionary.select(help_text, choices=commands))

    subcmd = cmd.get_command(ctx, subcommand_user)
    assert subcmd is not None
    ctx.protected_args = [subcommand_user]
    _process_parameters(ctx, cmd.params, unsafe_ask=unsafe_ask, show_help=show_help)

    ctx.invoked_subcommand = subcmd.name
    _invoke_cmd(ctx, cmd)

    with _make_context(subcmd, ctx) as sub_ctx:
        return _run_interactive(sub_ctx, subcmd, unsafe_ask=unsafe_ask, show_help=show_help)


def _run_interactive(ctx: click.Context, cmd: click.Command, *, unsafe_ask: bool, show_help: bool):
    if isinstance(cmd, click.MultiCommand):
        return _run_interactive_multi(ctx, cmd, unsafe_ask=unsafe_ask, show_help=show_help)
    elif isinstance(cmd, click.Command):
        _process_parameters(ctx, cmd.params, unsafe_ask=unsafe_ask, show_help=show_help)
        return _invoke_cmd(ctx, cmd)
    else:
        raise NotImplementedError


def _make_context(cmd: click.Command, parent: Context | None, **extra) -> Context:
    for key, value in cmd.context_settings.items():
        if key not in extra:
            extra[key] = value

    ctx = cmd.context_class(
        cmd,
        info_name=None,
        parent=parent,
        **extra,
    )

    return ctx


def run_interactive(
    cmd: click.Command,
    *,
    unsafe_ask: bool = True,
    exit_on_interrupt: bool = True,
    show_help: bool = True,
):
    with _make_context(cmd, None) as ctx:
        if unsafe_ask:
            try:
                return _run_interactive(ctx, cmd, unsafe_ask=unsafe_ask, show_help=show_help)
            except KeyboardInterrupt:
                questionary.print("Interrupted by user", style="bold red")
                if exit_on_interrupt:
                    sys.exit(1)
                else:
                    return None
        else:
            return _run_interactive(ctx, cmd, unsafe_ask=unsafe_ask, show_help=show_help)
