def parse(path, key, value) -> dict:
    # Initialize result
    result = {"key": key, "value": value}

    # Parse key
    key_out = value["@Name"]

    # Parse value
    value_out = value["Value"]
    # If empty, value_out is returned as None.
    # We need it as empty string
    if value_out is None:
        value_out = ""

    # Consolidate Result
    result["key"] = key_out
    result["value"] = value_out

    return result
