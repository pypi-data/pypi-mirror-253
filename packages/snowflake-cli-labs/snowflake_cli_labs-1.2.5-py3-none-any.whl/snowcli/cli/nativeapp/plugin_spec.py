from snowcli.api.plugin.command import (
    plugin_hook_impl,
    CommandSpec,
    SNOWCLI_ROOT_COMMAND_PATH,
    CommandType,
)
from snowcli.cli.nativeapp import commands


@plugin_hook_impl
def command_spec():
    return CommandSpec(
        parent_command_path=SNOWCLI_ROOT_COMMAND_PATH,
        command_type=CommandType.COMMAND_GROUP,
        typer_instance=commands.app,
    )
