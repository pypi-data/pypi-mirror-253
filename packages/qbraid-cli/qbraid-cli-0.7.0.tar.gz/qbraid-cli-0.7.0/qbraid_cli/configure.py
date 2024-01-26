"""
Update qbraidrc configuration file

"""
import configparser
import re
from pathlib import Path


def load_config():
    """Load the configuration from the file."""
    config_path = Path.home() / ".qbraid" / "qbraidrc"
    config = configparser.ConfigParser()
    config.read(config_path)
    return config


def save_config(config):
    """Save the configuration to the file."""
    config_path = Path.home() / ".qbraid" / "qbraidrc"
    with config_path.open("w") as configfile:
        config.write(configfile)


def validate_input(key, value):
    """Validate the user input based on the key."""
    if key == "url":
        if not re.match(r"^https?://\S+$", value):
            raise ValueError("Invalid URL format.")
    elif key == "email":
        if not re.match(r"^\S+@\S+\.\S+$", value):
            raise ValueError("Invalid email format.")
    return value


def prompt_for_config(config, section, key, default_values=None):
    """Prompt the user for a configuration setting, showing the current value as default."""
    default_values = default_values or {}
    current_value = config.get(section, key, fallback=default_values.get(key, ""))
    display_value = "None" if not current_value else current_value

    while True:
        try:
            new_value = input(f"Enter {key} [{display_value}]: ").strip()
            new_value = new_value or current_value
            return validate_input(key, new_value)
        except ValueError as e:
            print(f"Error: {e}")


def configure():
    """Prompt the user to configure each setting."""
    try:
        config = load_config()
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Error loading configuration: {e}")
        return

    section = "default"

    if section not in config:
        config[section] = {}

    default_values = {"url": "https://api.qbraid.com/api"}

    try:
        config[section]["url"] = prompt_for_config(
            config, section, "url", default_values
        )
        config[section]["email"] = prompt_for_config(
            config, section, "email", default_values
        )
        config[section]["api-key"] = prompt_for_config(
            config, section, "api-key", default_values
        )
        config[section]["refresh-token"] = prompt_for_config(
            config, section, "refresh-token", default_values
        )

        for key in list(config[section]):
            if not config[section][key]:
                del config[section][key]

        save_config(config)
        print("Configuration updated successfully.")
    except Exception as e:  # pylint: disable=broad-exception-caught
        print(f"Error updating configuration: {e}")
