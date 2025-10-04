# AI Tutor Orchestrator

A lightweight, high-accuracy orchestrator for educational AI tools.

## Quick Start

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Run the demo**
```bash
python demo.py
```

3. **Run the server**
```bash
python -m app.main
```

4. **Test the API**
```bash
curl -X POST "http://localhost:8000/orchestrate/message" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "test", "text": "I want practice problems on derivatives"}'
```

## Project Structure

```
orchestrator/
├─ app/
│  ├─ main.py                 # FastAPI app + endpoints
│  ├─ orchestrator.py         # core orchestration flow
│  ├─ intent.py               # intent detection module
│  ├─ extractor.py            # parameter extraction (LLM + parser)
│  ├─ validator.py            # schema validation helpers
│  ├─ tools/
│  │   ├─ note_maker.py
│  │   ├─ flashcard.py
│  │   └─ concept_explainer.py
│  ├─ state.py                # state manager (JSON-based)
│  └─ config.py
├─ tests/
│  └─ test_extraction.py
├─ data/
│  └─ examples.jsonl          # sample utterances + gold params
└─ README.md
```

## API Endpoints

- `POST /orchestrate/message` - Main orchestration endpoint
- `GET /health` - Health check

## Demo

The orchestrator handles these intents:
- **quiz_generator**: "I want practice problems on derivatives"
- **flashcard_generator**: "Make flashcards on photosynthesis"  
- **note_maker**: "I need notes on thermodynamics"
- **concept_explainer**: "Explain quantum mechanics simply"