from src.constants import ERROR_MSG


# Create a Model to handle the calculator's operation
def evaluateExpression(expression):
    """Evaluate an expression."""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG

    return result
