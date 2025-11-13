def validate_input(data):
    """Check that all values are numbers"""
    return all(isinstance(x, (int, float)) for x in data)
