from fastapi import FastAPI
from pydantic import BaseModel, Field
from prompt import SYS_PROMPT
import requests


app = FastAPI()

class EmailRequest(BaseModel):
    tone: str
    input: str
class EmailResponse(BaseModel):
    subject: str = Field(
        description="The subject of the email"
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
            "format": EmailResponse.model_json_schema()
        }
    )
    result = response.json()
    return {
        "email": result["response"]
    }