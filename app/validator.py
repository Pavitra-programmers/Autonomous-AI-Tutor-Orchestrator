"""Schema validation helpers using Pydantic."""

from pydantic import ValidationError

def validate_params(pydantic_model, data):
    try:
        obj = pydantic_model.parse_obj(data)
        return obj, None
    except ValidationError as e:
        # return errors to orchestrator so it can ask clarifying question
        return None, e.errors()