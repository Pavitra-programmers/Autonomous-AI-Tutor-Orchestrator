"""Concept explainer tool adapter."""

async def call_concept_tool(params: dict):
    """
    Generate concept explanations based on extracted parameters.
    Creates mock explanations for demo purposes.
    """
    concept = params["concept"]
    subject = params["subject"]
    style = params.get("style", "simple")
    
    return {
        "concept": concept,
        "subject": subject,
        "style": style,
        "explanation": f"This is a {style} explanation of {concept} in {subject}.",
        "adaptation_details": "adapted using student mastery level"
    }