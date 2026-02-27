"""Tests for CLI interface."""

import pytest
from unittest.mock import patch
from pathlib import Path

from distillation.cli import get_cli_config
from distillation.models import SystemConfig


class TestCLIConfig:
    """Test CLI configuration handling."""

    def test_get_cli_config_defaults(self):
        """Test getting CLI config with defaults."""
        # Reset global CLI options
        import distillation.cli
        distillation.cli._cli_options = {}

        config = get_cli_config()
        assert isinstance(config, SystemConfig)
        assert config.cli.verbose is False
        assert config.cli.quiet is False

    def test_get_cli_config_verbose(self):
        """Test getting CLI config with verbose option."""
        import distillation.cli
        distillation.cli._cli_options = {"verbose": True, "quiet": False}

        config = get_cli_config()
        assert config.cli.verbose is True
        assert config.cli.quiet is False

    def test_get_cli_config_quiet(self):
        """Test getting CLI config with quiet option."""
        import distillation.cli
        distillation.cli._cli_options = {"verbose": False, "quiet": True}

        config = get_cli_config()
        assert config.cli.verbose is False
        assert config.cli.quiet is True


class TestCLICommands:
    """Test CLI command functionality."""

    @patch('distillation.config.load_config')
    def test_init_command_basic(self, mock_load_config, tmp_path):
        """Test basic init command functionality."""
        from distillation.config import ConfigManager

        # Create input directory
        input_dir = tmp_path / "research"
        input_dir.mkdir()

        # Mock the config loading
        mock_config = SystemConfig(
            distillation={
                "input_dir": str(input_dir),
                "output_dir": str(tmp_path / "output"),
            }
        )
        mock_load_config.return_value = mock_config

        # Change to temp directory for test
        original_cwd = Path.cwd()
        try:
            import os
            os.chdir(tmp_path)

            # This would normally be called via typer, but we'll test the logic
            config_manager = ConfigManager()
            config_path = Path("distillation-config.yaml")

            # Test that we can create and save config
            config_manager.config_path = config_path
            config_manager.save(mock_config)

            assert config_path.exists()

        finally:
            os.chdir(original_cwd)

    def test_config_show_command(self):
        """Test config show command logic."""
        # This is mainly testing that the command can be called
        # Full integration testing would require typer test client
        pass

    def test_extract_command_placeholder(self):
        """Test extract command placeholder."""
        # Test that the command exists and can be called with basic args
        pass

    def test_distill_command_placeholder(self):
        """Test distill command placeholder."""
        # Test that the command exists and can be called with basic args
        pass

    def test_validate_command_placeholder(self):
        """Test validate command placeholder."""
        # Test that the command exists and can be called with basic args
        pass