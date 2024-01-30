from pathlib import Path
import click
import cloup


@cloup.group(help="An awesome CLI")
@cloup.option("--common-option", type=str, required=True, default="default", help="Common option")
@click.pass_context
def cli(ctx: click.Context, common_option: str):
    ctx.ensure_object(dict)

    ctx.obj["common_option"] = common_option


@cli.command("foo")
@cloup.option(
    "--single-choice-value", type=cloup.Choice(["a", "b", "c"]), required=True, default="a", help="Single choice"
)
@cloup.option(
    "--multi-choice-value", type=cloup.Choice(["a", "b", "c"]), required=True, multiple=True, default=["a", "b"]
)
@cloup.option("--path", type=cloup.Path(exists=True, dir_okay=False, path_type=Path), required=True)
@cloup.option("--value", type=int, required=True)
@cloup.option("--a-flag", is_flag=True, default=False, help="A flag")
def foo(**kwargs):
    click.echo(f"foo {kwargs}")


@cli.command()
@click.pass_context
def with_context(ctx: click.Context):
    common_option = ctx.obj["common_option"]
    click.echo(f"with-content {common_option}")


if __name__ == "__main__":
    from interactive_click import run_interactive

    run_interactive(cli)
