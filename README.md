# Multi-Tone Email Generator

A full-stack GenAI application that converts a user's rough
email requirements into a polished email using a selected tone.

## Features

- Formal, Casual, Aggressive and Empathetic tones
- Local LLM inference using Ollama
- FastAPI backend
- Pydantic request/response validation
- JSON structured output from the LLM
- HTML/CSS/JavaScript frontend
- CORS configuration
- Loading/disabled state while generating
- No external LLM API key required

## Architecture

┌─────────────────────────┐
│       Browser           │
│ HTML / CSS / JavaScript │
└────────────┬────────────┘
             │
             │ HTTP POST
             │ { tone, input }
             ▼
┌─────────────────────────┐
│        FastAPI          │
│                         │
│ Pydantic validation     │
│ Prompt construction     │
│ Error handling          │
└────────────┬────────────┘
             │
             │ HTTP POST
             ▼
┌─────────────────────────┐
│         Ollama          │
│                         │
│      Llama 3.2 3B      │
│                         │
│ JSON Schema             │
└────────────┬────────────┘
             │
             ▼
       ┌─────────────┐
       │ EmailResponse│
       │   subject    │
       │   body       │
       └─────────────┘


# start up guide for local 

### after cloning follow he below steps

step 1: create a venv 
python -m venv venv 

step 2 : run pip install -r requirements.txt

step 3: uvicorn app:app --reload