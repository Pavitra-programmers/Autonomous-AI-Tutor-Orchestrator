"""Schema validation helpers using Pydantic."""

from pydantic import ValidationError

def validate_params(pydantic_model, data):
    """
    Validate extracted parameters against Pydantic model.
    Returns validated object or error details for clarification.
    """
    try:
        obj = pydantic_model.parse_obj(data)
        return obj, None
    except ValidationError as e:
        # Return validation errors so orchestrator can ask clarifying questions
        return None, e.errors()