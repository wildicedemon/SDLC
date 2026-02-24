"""Command-line interface for the research distillation system."""

import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from .config import load_config
from .models import SystemConfig

# Initialize Typer app
app = typer.Typer(
    name="distill",
    help="Research distillation system for autonomous AI coding agents",
    add_completion=False,
)

# Initialize Rich console
console = Console()


def version_callback(value: bool) -> None:
    """Show version information."""
    if value:
        from . import __version__
        console.print(f"Research Distillation v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-V",
        help="Show version information",
        callback=version_callback,
        is_eager=True,
    ),
    config: Optional[Path] = typer.Option(
        None,
        "--config",
        "-c",
        help="Path to configuration file",
        exists=True,
        file_okay=True,
        dir_okay=False,
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose output",
    ),
    quiet: bool = typer.Option(
        False,
        "--quiet",
        "-q",
        help="Suppress non-error output",
    ),
) -> None:
    """Research distillation system for autonomous AI coding agents."""
    # Store CLI options in global state for use by subcommands
    global _cli_options
    _cli_options = {
        "config_path": config,
        "verbose": verbose,
        "quiet": quiet,
    }


_cli_options: dict = {}


def get_cli_config() -> SystemConfig:
    """Get configuration with CLI overrides."""
    config = load_config()

    # Apply CLI overrides
    if _cli_options.get("verbose"):
        config.cli.verbose = True
        config.cli.quiet = False
    if _cli_options.get("quiet"):
        config.cli.quiet = True
        config.cli.verbose = False

    return config


@app.command()
def init(
    input_dir: Path = typer.Option(
        ...,
        "--input-dir",
        "-i",
        help="Directory containing research files",
        exists=True,
        file_okay=False,
        dir_okay=True,
    ),
    output_dir: Path = typer.Option(
        "output",
        "--output-dir",
        "-o",
        help="Directory for generated outputs",
    ),
    force: bool = typer.Option(
        False,
        "--force",
        "-f",
        help="Overwrite existing configuration",
    ),
) -> None:
    """Initialize a new distillation project."""
    from .config import ConfigManager

    console.print("[bold blue]Initializing research distillation project...[/bold blue]")

    try:
        # Create config manager
        config_manager = ConfigManager()

        # Create initial configuration
        config = SystemConfig(
            distillation={
                "input_dir": str(input_dir),
                "output_dir": str(output_dir),
            }
        )

        # Save configuration
        config_path = Path("distillation-config.yaml")
        if config_path.exists() and not force:
            console.print(f"[yellow]Configuration file already exists: {config_path}[/yellow]")
            console.print("Use --force to overwrite")
            raise typer.Exit(1)

        config_manager.config_path = config_path
        config_manager.save(config)

        console.print(f"[green]✓[/green] Configuration saved to {config_path}")
        console.print(f"[green]✓[/green] Input directory: {input_dir}")
        console.print(f"[green]✓[/green] Output directory: {output_dir}")

        # Create output directory
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        console.print(f"[green]✓[/green] Created output directory: {output_path}")

    except Exception as e:
        console.print(f"[red]✗[/red] Initialization failed: {e}")
        raise typer.Exit(1)


@app.command()
def config(
    show: bool = typer.Option(
        False,
        "--show",
        "-s",
        help="Show current configuration",
    ),
    create_example: bool = typer.Option(
        False,
        "--create-example",
        help="Create example configuration file",
    ),
    output: Optional[Path] = typer.Option(
        None,
        "--output",
        "-o",
        help="Output path for example config",
    ),
) -> None:
    """Manage configuration."""
    from .config import ConfigManager

    if show:
        try:
            config = get_cli_config()
            console.print("[bold]Current Configuration:[/bold]")
            console.print_json(config.json(indent=2))
        except Exception as e:
            console.print(f"[red]✗[/red] Failed to load configuration: {e}")
            raise typer.Exit(1)

    elif create_example:
        try:
            config_manager = ConfigManager()
            output_path = output or Path("distillation-config.example.yaml")
            config_manager.create_example_config(output_path)
            console.print(f"[green]✓[/green] Example configuration created: {output_path}")
        except Exception as e:
            console.print(f"[red]✗[/red] Failed to create example config: {e}")
            raise typer.Exit(1)

    else:
        console.print("Use --show to display current config or --create-example to create an example")
        raise typer.Exit(1)


@app.command()
def extract(
    input_file: Optional[Path] = typer.Option(
        None,
        "--input",
        "-i",
        help="Specific input file to process",
        exists=True,
        file_okay=True,
        dir_okay=False,
    ),
    output_file: Optional[Path] = typer.Option(
        None,
        "--output",
        "-o",
        help="Output file for extracted atoms",
    ),
) -> None:
    """Extract knowledge atoms from research files."""
    console.print("[bold blue]Extracting knowledge atoms...[/bold blue]")

    try:
        config = get_cli_config()

        # This is a placeholder - actual extraction logic will be implemented later
        console.print("[yellow]⚠[/yellow] Extraction logic not yet implemented")
        console.print(f"Input directory: {config.distillation.input_dir}")
        console.print(f"Output directory: {config.distillation.output_dir}")

    except Exception as e:
        console.print(f"[red]✗[/red] Extraction failed: {e}")
        raise typer.Exit(1)


@app.command()
def distill(
    output_dir: Optional[Path] = typer.Option(
        None,
        "--output",
        "-o",
        help="Output directory for distilled products",
    ),
) -> None:
    """Run the complete distillation pipeline."""
    console.print("[bold blue]Running complete distillation pipeline...[/bold blue]")

    try:
        config = get_cli_config()

        # This is a placeholder - full pipeline will be implemented later
        console.print("[yellow]⚠[/yellow] Full distillation pipeline not yet implemented")
        console.print(f"Input directory: {config.distillation.input_dir}")
        output_dir = output_dir or config.distillation.output_dir
        console.print(f"Output directory: {output_dir}")

    except Exception as e:
        console.print(f"[red]✗[/red] Distillation failed: {e}")
        raise typer.Exit(1)


@app.command()
def validate(
    input_file: Path = typer.Option(
        ...,
        "--input",
        "-i",
        help="Product specification file to validate",
        exists=True,
        file_okay=True,
        dir_okay=False,
    ),
) -> None:
    """Validate product specifications."""
    console.print(f"[bold blue]Validating specification: {input_file}[/bold blue]")

    try:
        # This is a placeholder - validation logic will be implemented later
        console.print("[yellow]⚠[/yellow] Validation logic not yet implemented")
        console.print(f"Would validate: {input_file}")

    except Exception as e:
        console.print(f"[red]✗[/red] Validation failed: {e}")
        raise typer.Exit(1)


def main() -> None:
    """Entry point for the CLI application."""
    try:
        app()
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]Unexpected error: {e}[/red]")
        if _cli_options.get("verbose"):
            import traceback
            console.print(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()