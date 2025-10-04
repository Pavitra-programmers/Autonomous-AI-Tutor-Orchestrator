"""Quiz generator tool adapter."""

async def call_quiz_tool(params: dict):
    # for demo, generate quiz from topic
    topic = params["topic"]
    subject = params["subject"]
    num_questions = params.get("num_questions", 5)
    return {
        "topic": topic,
        "subject": subject,
        "questions": [
            {"question": f"What is {topic} question {i+1}?", "answer": f"Answer {i+1}"} 
            for i in range(num_questions)
        ],
        "adaptation_details": "adapted using student mastery level"
    }