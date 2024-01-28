def parse(path, key, value) -> dict:
    # Initialize result
    result = {"key": key, "value": value}

    # Parse key
    key_out = value["@Name"]

    # Parse value
    value_out = value["Value"]
    # As bool("False") would return True in python, we use below method
    if value_out == "True":
        value_out = True
    else:
        value_out = False

    # Consolidate Result
    result["key"] = key_out
    result["value"] = value_out

    return result
