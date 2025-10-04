"""Configuration settings."""

import os

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Model Settings
INTENT_MODEL = "facebook/bart-large-mnli"
INTENT_THRESHOLD = 0.5

# Tool Settings
DEFAULT_QUIZ_QUESTIONS = 5
DEFAULT_FLASHCARD_COUNT = 5

# State Management
STATE_FILE = "data/student_states.json"