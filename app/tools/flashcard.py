"""Flashcard tool adapter."""

async def call_flashcard_tool(params: dict):
    # for demo, build flashcards from topic
    topic = params["topic"]
    count = params.get("count", 5)
    return {
        "topic": topic,
        "flashcards": [
            {"question": f"What is {topic} Q{i+1}?", "answer": f"Answer {i+1}"} for i in range(count)
        ],
        "adaptation_details": "adapted using student mastery level"
    }