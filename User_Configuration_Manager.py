def add_setting(settings: dict, key_value_pair: tuple) -> str:
    key = str(key_value_pair[0]).lower()
    value = str(key_value_pair[1]).lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings: dict, key_value_pair: tuple) -> str:
    key = str(key_value_pair[0]).lower()
    value = str(key_value_pair[1]).lower()
    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings: dict, key: str) -> str:
    lower_key = str(key).lower()
    if lower_key in settings:
        del settings[lower_key]
        return f"Setting '{lower_key}' deleted successfully!"
    return "Setting not found!"

def view_settings(settings: dict) -> str:
    if not settings:
        return "No settings available."
    lines = ["Current User Settings:"]
    for key, value in settings.items():
        lines.append(f"{key.capitalize()}: {value}")
    return "\n".join(lines) + "\n"

test_settings = {
    'theme': 'dark',
    'notifications': 'enabled',
    'volume': 'high'
}
