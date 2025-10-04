"""Core orchestration flow."""

from app.intent import detect_intent
from app.extractor import extract_quiz_params, extract_flashcard_params, extract_note_params, extract_concept_params, QuizParams, FlashcardParams, NoteParams, ConceptParams
from app.validator import validate_params
from app.tools import flashcard, note_maker, concept_explainer, quiz_generator

async def orchestrate(user_id: str, text: str):
    """Main orchestration function."""
    
    # 1. detect intent
    intent, score = detect_intent(text)
    if intent == "unknown":
        return {"type": "clarify", "text": "I couldn't tell which tool you want — note maker, flashcards, or concept explainer?"}

    # 2. choose Pydantic model for that tool
    # 3. call extractor for model
    # 4. validate with validate_params
    # 5. if missing fields → return clarifying question
    # 6. else call adapter, normalize response, return to frontend
    
    if intent == "quiz_generator":
        params = extract_quiz_params(text)
        validated, errors = validate_params(QuizParams, params.dict())
        if errors:
            return {"type": "clarify", "text": "I need the topic and subject. Which topic?"}
        result = await quiz_generator.call_quiz_tool(validated.dict())
        return {"type": "result", "tool": "quiz_generator", "payload": result}
    
    elif intent == "flashcard_generator":
        params = extract_flashcard_params(text)
        validated, errors = validate_params(FlashcardParams, params.dict())
        if errors:
            return {"type": "clarify", "text": "I need the topic and subject. Which topic?"}
        result = await flashcard.call_flashcard_tool(validated.dict())
        return {"type": "result", "tool": "flashcard_generator", "payload": result}
    
    elif intent == "note_maker":
        params = extract_note_params(text)
        validated, errors = validate_params(NoteParams, params.dict())
        if errors:
            return {"type": "clarify", "text": "I need the topic and subject. Which topic?"}
        result = await note_maker.call_note_tool(validated.dict())
        return {"type": "result", "tool": "note_maker", "payload": result}
    
    elif intent == "concept_explainer":
        params = extract_concept_params(text)
        validated, errors = validate_params(ConceptParams, params.dict())
        if errors:
            return {"type": "clarify", "text": "I need the concept and subject. Which concept?"}
        result = await concept_explainer.call_concept_tool(validated.dict())
        return {"type": "result", "tool": "concept_explainer", "payload": result}
    
    return {"type": "error", "text": "Unknown intent"}