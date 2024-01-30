def hide_value(value):
    value_to_hide = "No password"
    if value is not None and len(value) > 4:
        value_to_hide = f"{value[0]}****{value[-1:]}"
    return value_to_hide
