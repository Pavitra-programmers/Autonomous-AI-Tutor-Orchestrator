"""Simple demo script for the AI Tutor Orchestrator."""

import asyncio
import json
from app.orchestrator import orchestrate

async def demo():
    """Run demo scenarios to showcase the orchestrator."""
    print("AI Tutor Orchestrator Demo")
    print("=" * 50)
    
    scenarios = [
        "I'm struggling with derivatives in calculus and want practice problems",
        "Make 5 flashcards on photosynthesis for biology", 
        "Explain quantum mechanics simply - I'm confused",
        "I need comprehensive notes on thermodynamics in physics"
    ]
    
    for i, text in enumerate(scenarios, 1):
        print(f"\nScenario {i}: {text}")
        print("-" * 50)
        
        try:
            result = await orchestrate("demo_user", text)
            print("Result:")
            print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"Error: {e}")
        
        print()

if __name__ == "__main__":
    asyncio.run(demo())