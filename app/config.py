"""Configuration settings for the orchestrator."""

import os

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Intent detection model settings
INTENT_MODEL = "facebook/bart-large-mnli"
INTENT_THRESHOLD = 0.5

# Default tool settings
DEFAULT_QUIZ_QUESTIONS = 5
DEFAULT_FLASHCARD_COUNT = 5

# File paths
STATE_FILE = "data/student_states.json"