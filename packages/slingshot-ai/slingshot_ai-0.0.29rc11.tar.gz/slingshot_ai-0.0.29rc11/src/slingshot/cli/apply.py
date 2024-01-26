from __future__ import annotations

from slingshot.cli.config.slingshot_cli import SlingshotCLIApp
from slingshot.sdk.slingshot_sdk import SlingshotSDK
from slingshot.sdk.utils import console

app = SlingshotCLIApp()


@app.command(name="apply", requires_project=True, top_level=True, requires_auth=True)
async def apply(*, sdk: SlingshotSDK) -> None:
    """Apply the local slingshot.yaml file for the current project by updating the remote."""
    any_changes = await sdk.apply_project()
    if not any_changes:
        console.print("[cyan]No changes applied[/cyan]")


@app.command(name="export", requires_project=True, top_level=True, requires_auth=True)
async def export(*, sdk: SlingshotSDK) -> None:
    """Export a YAML representation of the current project state and print it to the console."""
    await sdk.export_project(should_print=True)
