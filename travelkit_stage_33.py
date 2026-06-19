# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: TravelKit
TRAVELKIT_SETTINGS = {
    "currency": "USD",
    "default_packing_category": "clothes",
    "notification_enabled": True,
}


def update_settings(key: str, value):
    """Safely update a single setting without overwriting the whole dict."""
    if key in TRAVELKIT_SETTINGS and isinstance(value, (str, int, bool)):
        TRAVELKIT_SETTINGS[key] = value
        return True
    return False


def get_setting(key: str, default=None):
    """Retrieve a setting or return the provided default if missing."""
    return TRAVELKIT_SETTINGS.get(key, default)


def reset_settings():
    """Reset all settings to their initial values defined in the dictionary."""
    global TRAVELKIT_SETTINGS
    TRAVELKIT_SETTINGS = {
        "currency": "USD",
        "default_packing_category": "clothes",
        "notification_enabled": True,
    }
