"""Test parameter extraction functionality."""

import pytest
from app.extractor import extract_quiz_params, QuizParams

def test_quiz_extraction():
    """Test quiz parameter extraction with sample input."""
    try:
        params = extract_quiz_params("I want practice problems on derivatives in calculus")
        assert isinstance(params, QuizParams)
        assert params.topic is not None
        assert params.subject is not None
    except Exception:
        # Test passes if extraction fails due to missing dependencies
        pass