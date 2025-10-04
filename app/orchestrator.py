"""Core orchestration flow."""

from app.intent import detect_intent
from app.extractor import extract_quiz_params, extract_flashcard_params, extract_note_params, extract_concept_params, QuizParams, FlashcardParams, NoteParams, ConceptParams
from app.validator import validate_params
from app.tools import flashcard, note_maker, concept_explainer, quiz_generator

async def orchestrate(user_id: str, text: str):
    """
    Main orchestration function that processes user requests.
    Handles intent detection, parameter extraction, validation, and tool execution.
    """
    
    # Step 1: Detect user intent
    intent, score = detect_intent(text)
    if intent == "unknown":
        return {"type": "clarify", "text": "I couldn't tell which tool you want. Do you want notes, flashcards, practice problems, or an explanation?"}

    # Step 2: Extract parameters based on intent
    if intent == "quiz_generator":
        params = extract_quiz_params(text)
        validated, errors = validate_params(QuizParams, params.dict())
        if errors:
            return {"type": "clarify", "text": "I need the topic and subject. Which topic would you like to practice?"}
        result = await quiz_generator.call_quiz_tool(validated.dict())
        return {"type": "result", "tool": "quiz_generator", "payload": result}
    
    elif intent == "flashcard_generator":
        params = extract_flashcard_params(text)
        validated, errors = validate_params(FlashcardParams, params.dict())
        if errors:
            return {"type": "clarify", "text": "I need the topic and subject. Which topic would you like flashcards for?"}
        result = await flashcard.call_flashcard_tool(validated.dict())
        return {"type": "result", "tool": "flashcard_generator", "payload": result}
    
    elif intent == "note_maker":
        params = extract_note_params(text)
        validated, errors = validate_params(NoteParams, params.dict())
        if errors:
            return {"type": "clarify", "text": "I need the topic and subject. Which topic would you like notes for?"}
        result = await note_maker.call_note_tool(validated.dict())
        return {"type": "result", "tool": "note_maker", "payload": result}
    
    elif intent == "concept_explainer":
        params = extract_concept_params(text)
        validated, errors = validate_params(ConceptParams, params.dict())
        if errors:
            return {"type": "clarify", "text": "I need the concept and subject. Which concept would you like me to explain?"}
        result = await concept_explainer.call_concept_tool(validated.dict())
        return {"type": "result", "tool": "concept_explainer", "payload": result}
    
    return {"type": "error", "text": "Unknown intent"}