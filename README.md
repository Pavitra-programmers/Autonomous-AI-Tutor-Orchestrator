# AI Tutor Orchestrator

A simple orchestrator that routes student requests to appropriate educational tools. Built for hackathon demonstration.

## Getting Started

First, install the required packages:

```bash
pip install -r requirements.txt
```

Then run the demo to see it in action:

```bash
python demo.py
```

To start the API server:

```bash
python -m app.main
```

The server will be available at http://localhost:8000. You can test it with:

```bash
curl -X POST "http://localhost:8000/orchestrate/message" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "test", "text": "I want practice problems on derivatives"}'
```

## How It Works

The orchestrator takes a student's message and:

1. Detects what type of help they need (quiz, flashcards, notes, or explanation)
2. Extracts relevant parameters like topic and subject
3. Validates the parameters
4. Calls the appropriate tool to generate content

## Project Structure

```
orchestrator/
├─ app/
│  ├─ main.py                 # FastAPI endpoints
│  ├─ orchestrator.py         # main orchestration logic
│  ├─ intent.py               # detects user intent
│  ├─ extractor.py            # extracts parameters from text
│  ├─ validator.py            # validates extracted parameters
│  ├─ tools/                  # tool adapters
│  │   ├─ note_maker.py
│  │   ├─ flashcard.py
│  │   ├─ concept_explainer.py
│  │   └─ quiz_generator.py
│  ├─ state.py                # manages student state
│  └─ config.py               # configuration settings
├─ tests/
│  └─ test_extraction.py
├─ data/
│  └─ examples.jsonl
└─ README.md
```

## Supported Tools

The orchestrator can route to four different tools:

- **Quiz Generator**: Creates practice questions and quizzes
- **Flashcard Generator**: Generates study flashcards  
- **Note Maker**: Creates study notes and summaries
- **Concept Explainer**: Provides explanations of concepts

## Example Usage

Try these sample requests:

- "I want practice problems on derivatives in calculus"
- "Make 5 flashcards on photosynthesis for biology"
- "Explain quantum mechanics simply"
- "I need comprehensive notes on thermodynamics"

The orchestrator will detect the intent, extract parameters, and generate appropriate content.