from pydantic import BaseModel

class TranscriptRequest(BaseModel):
    youtube_url: str

class AskQuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str