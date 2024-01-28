import collections
import sys
from dataclasses import dataclass
from typing import Annotated, Optional

import jinja2
import typer
import yaml
from click import ClickException
from jinja2 import ChainableUndefined, Environment, StrictUndefined, Undefined

app = typer.Typer(rich_markup_mode="rich")


@dataclass
class Mapping:
    key: str
    value: str

    @classmethod
    def parse(cls, value: str) -> 'Mapping':
        key, value = value.split("=")
        return Mapping(key, value)


@app.command(
    help="Renders the Jinja template given in TEMPLATE_FILE using a context built from YAML files and "
         "mappings supplied on the command line.",
    epilog="In case context variables appear in multiple YAML files, values from subsequent files take precedence. "
           "Values explicitly specified always take precedence over values from YAML files.\n\n\n\n"
           "Any variables referenced in the template but not provided in the context will be treated based on the "
           "specified mode:\n\n\n\n"
           "[yellow bold]STRICT MODE[/yellow bold]: Undefined variables can only be checked for definedness. "
           "Any other access raises an error.\n\n"
           "[yellow bold]DEFAULT MODE[/yellow bold]: Undefined variables are treated as an empty string when printed "
           "and as an empty list when iterated over. Any other access raises an error.\n\n"
           "[yellow bold]LENIENT MODE[/yellow bold]: In addition to the default mode, attribute access and indexing "
           "are allowed, and they return a new undefined variable which is then also treated in LENIENT MODE.",
)
def render(
        *,
        template_file: Annotated[typer.FileText, typer.Argument(
            help="Path to the jinja template file.",
        )],
        context_values: Annotated[Optional[list[Mapping]], typer.Argument(
            metavar="CONTEXT",
            parser=Mapping.parse,
            help="Context values in the format 'key=value'.",
        )] = None,
        context_files: Annotated[Optional[list[typer.FileText]], typer.Option(
            "--context-file", '-f',
            help="Path to a YAML context file. (optional, multiple may be given)",
        )] = None,
        extensions: Annotated[Optional[list[str]], typer.Option(
            "--extension", '-e',
            help="Import path of a Jinja2 extension (optional, multiple may be given)",
        )] = None,
        strict: Annotated[bool, typer.Option(
            "--strict", '-s',
            help="Strict mode. Forbids access of undefined variables (see below).",
        )] = False,
        lenient: Annotated[bool, typer.Option(
            "--lenient", '-l',
            help="Lenient mode. Allows indexing and attribute access of undefined variables (see below).",
        )] = False,
):
    # Build undefined variable
    if strict:
        undefined = StrictUndefined
    elif lenient:
        undefined = ChainableUndefined
    else:
        undefined = Undefined

    # Build environment
    env = Environment(
        autoescape=False,  # noqa: S701
        undefined=undefined,
        extensions=extensions,
    )

    # Build template
    try:
        template = env.from_string(template_file.read())
    except jinja2.exceptions.TemplateSyntaxError as err:
        raise ClickException(f"The template file does not contain a valid jinja template: {err.message}") from err

    # Build empty context
    context = {}

    # Add context from context files.
    for context_file in context_files:
        try:
            extra_context = yaml.safe_load(context_file.read() if context_file else sys.stdin)
        except yaml.YAMLError as err:
            raise ClickException(f"The context does not contain valid YAML syntax: {err}") from err

        if not isinstance(extra_context, collections.abc.Collection):
            raise ClickException("The context must be a dictionary, not a list or a scalar.")

        context.update(extra_context)

    # Add context from command line mappings
    for mapping in context_values:
        context[mapping.key] = mapping.value

    # Render template with context
    try:
        print(template.render(**context))  # noqa: T201
    except jinja2.exceptions.UndefinedError as err:
        raise ClickException(f"The context is missing a name used in the template: {err.message}") from err
