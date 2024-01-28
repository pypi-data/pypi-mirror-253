def parse(path, key, value) -> dict:
    # Initialize result
    result = {"key": key, "value": value}

    # Parse key
    key_out = value["@Name"]

    # Parse value
    value_out = float(value["Value"])

    # Consolidate Result
    result["key"] = key_out
    result["value"] = value_out

    return result
