def parse(path, key, value) -> dict:
    # Initialize result
    result = {"key": key, "value": value}

    # Parse key
    if "@Name" in value.keys():
        key_out = value["@Name"]
    else:
        key_out = key

    # Parse value
    if "Prop" in value.keys():
        # If Prop is present, use its value.
        value_out = value["Prop"]
    else:
        # If not, find all keys without @
        value_out = {k: v for k, v in value.items() if "@" not in k and k != "Attributes"}

    # Consolidate Result
    result["key"] = key_out
    result["value"] = value_out
    return result
