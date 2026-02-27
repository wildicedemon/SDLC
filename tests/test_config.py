"""Tests for configuration management."""

import pytest
import tempfile
from pathlib import Path
from unittest.mock import patch

from distillation.config import ConfigManager
from distillation.models import SystemConfig, DistillationConfig


class TestConfigManager:
    """Test ConfigManager functionality."""

    def test_config_manager_initialization(self):
        """Test config manager initialization."""
        manager = ConfigManager()
        assert manager.config_path is None
        assert not manager.is_loaded

    def test_config_manager_with_path(self):
        """Test config manager with specified path."""
        config_path = Path("test-config.yaml")
        manager = ConfigManager(config_path)
        assert manager.config_path == config_path

    def test_find_config_file(self):
        """Test finding configuration file in default locations."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            # Create a config file in one of the default locations
            config_file = temp_path / "distillation-config.yaml"
            config_file.write_text("distillation:\n  input_dir: test\n  output_dir: output\n")

            with patch("distillation.config.manager.ConfigManager.DEFAULT_CONFIG_PATHS",
                      [config_file]):
                manager = ConfigManager()
                found_path = manager._find_config_file()
                assert found_path == config_file

    def test_load_default_config(self):
        """Test loading default configuration when no file exists."""
        manager = ConfigManager()

        # Mock the research directory finding
        with patch.object(manager, '_find_research_directory', return_value=Path("mock-research")):
            config = manager.load()

            assert isinstance(config, SystemConfig)
            assert config.distillation.input_dir == Path("mock-research")
            assert config.distillation.output_dir == Path("output")
            assert manager.is_loaded

    def test_load_from_yaml_file(self):
        """Test loading configuration from YAML file."""
        import tempfile

        with tempfile.TemporaryDirectory() as temp_dir:
            research_dir = Path(temp_dir) / "research"
            output_dir = Path(temp_dir) / "output"
            research_dir.mkdir()
            output_dir.mkdir()

            config_data = f"""
distillation:
  input_dir: "{research_dir}"
  output_dir: "{output_dir}"
  max_file_size: 5242880
extraction:
  context_window: 5
"""

            with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
                f.write(config_data)
                config_path = Path(f.name)

            try:
                manager = ConfigManager(config_path)
                config = manager.load()

                assert config.distillation.input_dir == research_dir
                assert config.distillation.output_dir == output_dir
                assert config.distillation.max_file_size == 5242880
                assert config.extraction.context_window == 5
            finally:
                config_path.unlink()

    def test_save_config(self):
        """Test saving configuration to file."""
        import tempfile

        with tempfile.TemporaryDirectory() as temp_dir:
            research_dir = Path(temp_dir) / "test-research"
            output_dir = Path(temp_dir) / "test-output"
            research_dir.mkdir()
            output_dir.mkdir()

            with tempfile.NamedTemporaryFile(suffix='.yaml', delete=False) as f:
                config_path = Path(f.name)

            try:
                manager = ConfigManager(config_path)

                # Create a test config
                test_config = SystemConfig(
                    distillation=DistillationConfig(
                        input_dir=research_dir,
                        output_dir=output_dir,
                    )
                )

                # Save it
                manager.save(test_config)

                # Verify file was created and contains correct data
                assert config_path.exists()

                # Load it back
                loaded_config = SystemConfig.from_yaml(config_path)
                assert loaded_config.distillation.input_dir == research_dir
                assert loaded_config.distillation.output_dir == output_dir

            finally:
                if config_path.exists():
                    config_path.unlink()

    def test_get_config_value(self):
        """Test getting configuration values by key."""
        import tempfile

        with tempfile.TemporaryDirectory() as temp_dir:
            research_dir = Path(temp_dir) / "test-research"
            research_dir.mkdir()

            manager = ConfigManager()

            with patch.object(manager, '_find_research_directory', return_value=research_dir):
                config = manager.load()

                # Test getting existing values
                assert manager.get("distillation.input_dir") == research_dir
                assert manager.get("distillation.max_file_size") == 10 * 1024 * 1024

                # Test getting with default
                assert manager.get("nonexistent.key", "default") == "default"

                # Test getting nested values
                assert manager.get("extraction.context_window") == 3

    def test_set_config_value(self):
        """Test setting configuration values by key."""
        import tempfile

        with tempfile.TemporaryDirectory() as temp_dir:
            research_dir = Path(temp_dir) / "test-research"
            research_dir.mkdir()

            manager = ConfigManager()

            with patch.object(manager, '_find_research_directory', return_value=research_dir):
                config = manager.load()

                # Set a value
                manager.set("distillation.max_file_size", 20 * 1024 * 1024)

                # Verify it was set
                assert manager.get("distillation.max_file_size") == 20 * 1024 * 1024

                # Set nested value
                manager.set("extraction.context_window", 10)
                assert manager.get("extraction.context_window") == 10

    def test_update_from_dict(self):
        """Test updating configuration from dictionary."""
        import tempfile

        with tempfile.TemporaryDirectory() as temp_dir:
            research_dir = Path(temp_dir) / "test-research"
            research_dir.mkdir()

            manager = ConfigManager()

            with patch.object(manager, '_find_research_directory', return_value=research_dir):
                config = manager.load()

                # Update with nested dict
                updates = {
                    "distillation": {
                        "max_file_size": 30 * 1024 * 1024,
                        "supported_formats": ["md", "html", "pdf"]
                    },
                    "extraction": {
                        "context_window": 7
                    }
                }

                manager.update_from_dict(updates)

                # Verify updates
                assert manager.get("distillation.max_file_size") == 30 * 1024 * 1024
                assert "pdf" in manager.get("distillation.supported_formats")
                assert manager.get("extraction.context_window") == 7

    def test_create_example_config(self):
        """Test creating example configuration file."""
        import tempfile

        with tempfile.TemporaryDirectory() as temp_dir:
            research_dir = Path(temp_dir) / "research"
            research_dir.mkdir()

            with tempfile.NamedTemporaryFile(suffix='.yaml', delete=False) as f:
                example_path = Path(f.name)

            try:
                manager = ConfigManager()
                # Mock the research directory finding to return our temp directory
                with patch.object(manager, '_find_research_directory', return_value=research_dir):
                    manager.create_example_config(example_path)

                    # Verify file was created
                    assert example_path.exists()

                    # Verify it contains valid config
                    example_config = SystemConfig.from_yaml(example_path)
                    assert isinstance(example_config, SystemConfig)
                    assert example_config.distillation.input_dir == research_dir

            finally:
                if example_path.exists():
                    example_path.unlink()

    def test_invalid_config_file(self):
        """Test handling of invalid configuration files."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write("invalid: yaml: content: [\n")  # Invalid YAML
            invalid_path = Path(f.name)

        try:
            manager = ConfigManager(invalid_path)

            with pytest.raises(ValueError, match="Failed to load config"):
                manager.load()

        finally:
            invalid_path.unlink()

    def test_save_without_config(self):
        """Test attempting to save without loaded config."""
        manager = ConfigManager()

        with pytest.raises(ValueError, match="No configuration to save"):
            manager.save()


class TestGlobalConfigFunctions:
    """Test global configuration functions."""

    def test_get_config_manager(self):
        """Test getting global config manager instance."""
        from distillation.config import get_config_manager

        manager1 = get_config_manager()
        manager2 = get_config_manager()

        # Should return the same instance
        assert manager1 is manager2

    def test_load_config(self):
        """Test global load_config function."""
        from distillation.config import load_config

        config = load_config()
        assert isinstance(config, SystemConfig)

    def test_save_config(self):
        """Test global save_config function."""
        from distillation.config import save_config, load_config

        # Load current config
        original_config = load_config()

        # This should not raise an error (though it may not actually save if no path is set)
        save_config(original_config)