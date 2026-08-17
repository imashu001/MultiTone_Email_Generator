from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmailRequest(BaseModel):
    tone: str
    input: str
class EmailResponse(BaseModel):
    subject: str = Field(
        description="Only The subject of the email or a very short one liner to understand what email is about "
    )
    body: str = Field(
        description="The complete body of the email"
    )

@app.post("/")
def generate_email(request: EmailRequest):
    prompt = f"""
        You are an email writing assistant.

        Rewrite the user's email using a {request.tone} tone.

        The available tones are:
        - formal
        - casual
        - aggressive
        - empathetic

        Return ONLY the rewritten email.
        Do not explain your response.
        Do not mention that you are an AI.

        User's email:
        {request.input}
    """
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False,
            "tempreature": 1,
            "format": EmailResponse.model_json_schema()
        }
    )
    result = response.json()

    email = EmailResponse.model_validate_json(
        result["response"]
    )

    return email