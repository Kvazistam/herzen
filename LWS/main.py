from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
from schemas import StoryRequest, StoryResponse
from services.story_service import StoryService

app = FastAPI()
service = StoryService()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/generate", response_model=StoryResponse)
def generate_story(data: StoryRequest, db: Session = Depends(get_db)):
    user_id = 1
    story = service.generate_story(db, user_id, data)
    return story