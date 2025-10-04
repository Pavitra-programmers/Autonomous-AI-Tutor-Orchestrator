"""Intent detection module using keyword matching and Hugging Face."""

from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
CANDIDATE_LABELS = ["quiz_generator", "flashcard_generator", "concept_explainer", "note_maker"]

def detect_intent(text: str, threshold=0.5):
    text_lower = text.lower()
    
    # First try keyword matching for better accuracy
    if any(word in text_lower for word in ["practice problems", "quiz", "questions", "test", "exam", "problems"]):
        return "quiz_generator", 0.9
    
    if any(word in text_lower for word in ["flashcard", "flash card", "cards", "study cards"]):
        return "flashcard_generator", 0.9
    
    if any(word in text_lower for word in ["explain", "what is", "how does", "concept", "understand"]):
        return "concept_explainer", 0.9
    
    if any(word in text_lower for word in ["notes", "note", "summary", "outline", "comprehensive"]):
        return "note_maker", 0.9
    
    # Fallback to Hugging Face model
    try:
        res = classifier(text, candidate_labels=CANDIDATE_LABELS)
        top_label, score = res["labels"][0], res["scores"][0]
        if score < threshold:
            return "unknown", score
        return top_label, score
    except:
        return "unknown", 0.0