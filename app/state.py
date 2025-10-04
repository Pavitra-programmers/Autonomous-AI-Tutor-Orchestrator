"""State manager using JSON files."""

import json
import os
from typing import Dict, Any

def get_student_state(user_id: str) -> Dict[str, Any]:
    """Get student state from JSON file."""
    state_file = "data/student_states.json"
    
    # Create data directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Load existing states
    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            states = json.load(f)
    else:
        states = {}
    
    # Return student state or create default
    if user_id in states:
        return states[user_id]
    else:
        default_state = {
            "user_id": user_id,
            "learning_style": "visual",
            "emotional_state": "neutral",
            "mastery_level": 2
        }
        states[user_id] = default_state
        
        # Save updated states
        with open(state_file, 'w') as f:
            json.dump(states, f, indent=2)
        
        return default_state

def save_student_state(user_id: str, state: Dict[str, Any]):
    """Save student state to JSON file."""
    state_file = "data/student_states.json"
    
    # Load existing states
    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            states = json.load(f)
    else:
        states = {}
    
    # Update state
    states[user_id] = state
    
    # Save updated states
    with open(state_file, 'w') as f:
        json.dump(states, f, indent=2)