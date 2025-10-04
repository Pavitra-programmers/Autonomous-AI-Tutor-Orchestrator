"""Note maker tool adapter."""

async def call_note_tool(params: dict):
    # for demo, create notes from topic
    topic = params["topic"]
    subject = params["subject"]
    style = params.get("style", "comprehensive")
    return {
        "topic": topic,
        "subject": subject,
        "style": style,
        "content": f"# {topic} Notes\n\nThis is {style} notes about {topic} in {subject}.",
        "adaptation_details": "adapted using student mastery level"
    }