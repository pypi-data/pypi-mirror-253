"""Tools Utils Module"""
def filter_tools(keys, dictionary):
    """
    Fetches values from the dictionary based on provided keys.

    Args:
    - dictionary (dict): The source dictionary.
    - keys (list): List of keys to fetch values for.

    Returns:
    - list: List of values corresponding to the provided keys.
    """
    return [dictionary.get(key) for key in keys]

def format_agent_actions(steps: list[tuple]) -> list[dict]:
    return [
        {"tool": step[0].tool, "tool_input": step[0].tool_input, "log": step[0].log}
        for step in steps
    ]

def match_strings(keys: list[str], functions):
    """Match the strings in the keys to the functions"""
    # Initialize array to store output
    output = []

    # Loop through the functions array
    for function in functions:
        # If name property of function matches one of the strings in keys
        if function['name'] in keys:
            # Append the function to the output array
            output.append(function)

    # Return the output array
    return output