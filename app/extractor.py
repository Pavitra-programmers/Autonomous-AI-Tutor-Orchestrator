"""Parameter extraction using simple keyword matching."""

from pydantic import BaseModel
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
    """Extract quiz parameters from user text using keyword matching."""
    text_lower = user_text.lower()
    
    # Extract topic based on common subjects
    if "derivative" in text_lower:
        topic = "derivatives"
    elif "algebra" in text_lower:
        topic = "algebra"
    else:
        topic = "derivatives"  # default
    
    # Extract subject
    if "calculus" in text_lower:
        subject = "calculus"
    elif "math" in text_lower:
        subject = "math"
    else:
        subject = "calculus"  # default
    
    # Determine difficulty from context
    if any(word in text_lower for word in ["struggling", "confused", "help", "beginner"]):
        difficulty = "beginner"
    elif any(word in text_lower for word in ["advanced", "expert"]):
        difficulty = "advanced"
    else:
        difficulty = "medium"
    
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
    
    # Extract topic
    if "photosynthesis" in text_lower:
        topic = "photosynthesis"
    elif "thermodynamics" in text_lower:
        topic = "thermodynamics"
    else:
        topic = "photosynthesis"  # default
    
    # Extract subject
    if "biology" in text_lower:
        subject = "biology"
    elif "physics" in text_lower:
        subject = "physics"
    else:
        subject = "biology"  # default
    
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
    
    # Extract topic
    if "thermodynamics" in text_lower:
        topic = "thermodynamics"
    elif "photosynthesis" in text_lower:
        topic = "photosynthesis"
    else:
        topic = "thermodynamics"  # default
    
    # Extract subject
    if "physics" in text_lower:
        subject = "physics"
    elif "biology" in text_lower:
        subject = "biology"
    else:
        subject = "physics"  # default
    
    # Extract style
    if "comprehensive" in text_lower:
        style = "comprehensive"
    elif "summary" in text_lower:
        style = "summary"
    else:
        style = "comprehensive"  # default
    
    return NoteParams(
        topic=topic,
        subject=subject,
        style=style
    )

def extract_concept_params(user_text: str) -> ConceptParams:
    """Extract concept parameters from user text."""
    text_lower = user_text.lower()
    
    # Extract concept
    if "quantum" in text_lower:
        concept = "quantum mechanics"
    elif "photosynthesis" in text_lower:
        concept = "photosynthesis"
    else:
        concept = "quantum mechanics"  # default
    
    # Extract subject
    if "physics" in text_lower:
        subject = "physics"
    elif "biology" in text_lower:
        subject = "biology"
    else:
        subject = "physics"  # default
    
    # Extract style
    if "simple" in text_lower:
        style = "simple"
    elif "detailed" in text_lower:
        style = "detailed"
    else:
        style = "simple"  # default
    
    return ConceptParams(
        concept=concept,
        subject=subject,
        style=style
    )