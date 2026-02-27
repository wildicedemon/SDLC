"""Configuration management system."""

import os
from pathlib import Path
from typing import Dict, Optional, Any, Union
from pydantic import ValidationError

from ..models import SystemConfig, DistillationConfig


class ConfigManager:
    """Manages loading and saving of system configuration."""

    DEFAULT_CONFIG_PATHS = [
        Path("distillation-config.yaml"),
        Path("distillation-config.yml"),
        Path(".distillation/config.yaml"),
        Path(".distillation/config.yml"),
        Path("config/distillation.yaml"),
        Path("config/distillation.yml"),
    ]

    def __init__(self, config_path: Optional[Path] = None):
        """Initialize config manager.

        Args:
            config_path: Path to configuration file. If None, searches default locations.
        """
        self.config_path = config_path or self._find_config_file()
        self._config: Optional[SystemConfig] = None

    def _find_config_file(self) -> Optional[Path]:
        """Find configuration file in default locations."""
        for path in self.DEFAULT_CONFIG_PATHS:
            if path.exists():
                return path
        return None

    def load(self) -> SystemConfig:
        """Load configuration from file or create default.

        Returns:
            SystemConfig: The loaded or default configuration.
        """
        if self._config is not None:
            return self._config

        if self.config_path and self.config_path.exists():
            try:
                self._config = SystemConfig.from_yaml(self.config_path)
            except (ValidationError, OSError) as e:
                raise ValueError(f"Failed to load config from {self.config_path}: {e}")
        else:
            # Create default configuration
            self._config = self._create_default_config()

        return self._config

    def save(self, config: Optional[SystemConfig] = None) -> None:
        """Save configuration to file.

        Args:
            config: Configuration to save. If None, saves current config.
        """
        if config is not None:
            self._config = config

        if self._config is None:
            raise ValueError("No configuration to save")

        if self.config_path is None:
            self.config_path = self.DEFAULT_CONFIG_PATHS[0]

        # Ensure parent directory exists
        self.config_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            self._config.to_yaml(self.config_path)
        except OSError as e:
            raise ValueError(f"Failed to save config to {self.config_path}: {e}")

    def _create_default_config(self) -> SystemConfig:
        """Create default system configuration."""
        # Try to find research directory
        research_dir = self._find_research_directory()

        return SystemConfig(
            distillation=DistillationConfig(
                input_dir=research_dir or Path("research"),
                output_dir=Path("output"),
            )
        )

    def _find_research_directory(self) -> Optional[Path]:
        """Find research directory in common locations."""
        candidates = [
            Path("research"),
            Path("docs/research"),
            Path("Kimi-Research"),
            Path("docs"),
            Path("papers"),
        ]

        for candidate in candidates:
            if candidate.exists() and candidate.is_dir():
                return candidate

        return None

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value by dot-separated key.

        Args:
            key: Dot-separated configuration key (e.g., 'distillation.max_file_size')
            default: Default value if key not found

        Returns:
            Configuration value or default
        """
        config = self.load()
        keys = key.split('.')
        value = config.dict()

        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default

    def set(self, key: str, value: Any) -> None:
        """Set configuration value by dot-separated key.

        Args:
            key: Dot-separated configuration key
            value: Value to set
        """
        config = self.load()
        keys = key.split('.')
        config_dict = config.dict()

        # Navigate to the parent of the target key
        target = config_dict
        for k in keys[:-1]:
            if k not in target:
                target[k] = {}
            target = target[k]

        # Set the value
        target[keys[-1]] = value

        # Re-validate and update config
        self._config = SystemConfig(**config_dict)

    def update_from_dict(self, updates: Dict[str, Any]) -> None:
        """Update configuration from dictionary.

        Args:
            updates: Dictionary of configuration updates
        """
        config = self.load()
        config_dict = config.dict()

        def update_nested_dict(target: Dict[str, Any], source: Dict[str, Any]) -> None:
            """Recursively update nested dictionary."""
            for key, value in source.items():
                if isinstance(value, dict) and key in target and isinstance(target[key], dict):
                    update_nested_dict(target[key], value)
                else:
                    target[key] = value

        update_nested_dict(config_dict, updates)
        self._config = SystemConfig(**config_dict)

    def create_example_config(self, output_path: Path) -> None:
        """Create an example configuration file.

        Args:
            output_path: Path to save the example config
        """
        example_config = SystemConfig(
            distillation=DistillationConfig(
                input_dir=Path("research"),
                output_dir=Path("output"),
                max_file_size=50 * 1024 * 1024,  # 50MB
                supported_formats=["md", "markdown", "html", "json", "csv", "txt", "pdf"],
            )
        )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        example_config.to_yaml(output_path)

    @property
    def config_path(self) -> Optional[Path]:
        """Get current configuration file path."""
        return self._config_path

    @config_path.setter
    def config_path(self, value: Optional[Path]) -> None:
        """Set configuration file path."""
        self._config_path = value

    @property
    def is_loaded(self) -> bool:
        """Check if configuration is loaded."""
        return self._config is not None


# Global config manager instance
_config_manager: Optional[ConfigManager] = None


def get_config_manager() -> ConfigManager:
    """Get the global configuration manager instance."""
    global _config_manager
    if _config_manager is None:
        _config_manager = ConfigManager()
    return _config_manager


def load_config() -> SystemConfig:
    """Load system configuration."""
    return get_config_manager().load()


def save_config(config: Optional[SystemConfig] = None) -> None:
    """Save system configuration."""
    get_config_manager().save(config)