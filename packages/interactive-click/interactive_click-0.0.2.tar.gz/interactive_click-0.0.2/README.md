# interactive-click

## Installation

```console
pip install interactive-click
```

## Usage

```python
import click

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def cli(name):
    click.echo('Hello %s!' % name)

if __name__ == '__main__':
    import sys
    
    # Can be simply run by:
    #     run_interactive(cli)
    # But we can also wrap it by checking whether the user is running the script without any arguments
    if len(sys.argv) == 1:
        # No arguments, run interactive mode
        try:
            from interactive_click import run_interactive

            run_interactive(cli)
        except ImportError:
            cli()

    else:
        cli()

```

