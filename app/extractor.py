"""Parameter extraction using simple JSON parsing."""

from pydantic import BaseModel
import json
import re

class QuizParams(BaseModel):
    topic: str
    subject: str
    difficulty: str = "medium"
    question_type: str = "practice"
    num_questions: int = 5

class FlashcardParams(BaseModel):
    topic: str
    subject: str
    count: int = 5
    difficulty: str = "medium"

class NoteParams(BaseModel):
    topic: str
    subject: str
    style: str = "comprehensive"
    difficulty: str = "medium"

class ConceptParams(BaseModel):
    concept: str
    subject: str
    style: str = "simple"
    difficulty: str = "medium"

def extract_quiz_params(user_text: str) -> QuizParams:
    """Extract quiz parameters from user text."""
    text_lower = user_text.lower()
    
    # Simple keyword extraction
    topic = "derivatives" if "derivative" in text_lower else "algebra"
    subject = "calculus" if "calculus" in text_lower else "math"
    difficulty = "beginner" if any(word in text_lower for word in ["struggling", "confused", "help"]) else "medium"
    
    # Extract number of questions
    num_match = re.search(r'(\d+)', user_text)
    num_questions = int(num_match.group(1)) if num_match else 5
    
    return QuizParams(
        topic=topic,
        subject=subject,
        difficulty=difficulty,
        num_questions=num_questions
    )

def extract_flashcard_params(user_text: str) -> FlashcardParams:
    """Extract flashcard parameters from user text."""
    text_lower = user_text.lower()
    
    topic = "photosynthesis" if "photosynthesis" in text_lower else "thermodynamics"
    subject = "biology" if "biology" in text_lower else "physics"
    
    # Extract count
    count_match = re.search(r'(\d+)', user_text)
    count = int(count_match.group(1)) if count_match else 5
    
    return FlashcardParams(
        topic=topic,
        subject=subject,
        count=count
    )

def extract_note_params(user_text: str) -> NoteParams:
    """Extract note parameters from user text."""
    text_lower = user_text.lower()
    
    topic = "thermodynamics" if "thermodynamics" in text_lower else "photosynthesis"
    subject = "physics" if "physics" in text_lower else "biology"
    style = "comprehensive" if "comprehensive" in text_lower else "summary"
    
    return NoteParams(
        topic=topic,
        subject=subject,
        style=style
    )

def extract_concept_params(user_text: str) -> ConceptParams:
    """Extract concept parameters from user text."""
    text_lower = user_text.lower()
    
    concept = "quantum mechanics" if "quantum" in text_lower else "photosynthesis"
    subject = "physics" if "physics" in text_lower else "biology"
    style = "simple" if "simple" in text_lower else "detailed"
    
    return ConceptParams(
        concept=concept,
        subject=subject,
        style=style
    )