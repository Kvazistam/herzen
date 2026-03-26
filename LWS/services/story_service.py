from sqlalchemy.orm import Session
from models import Story
from llm_service import LLMService

class StoryService:
    def __init__(self):
        self.llm = LLMService()

    def build_prompt(self, genre: str, characters):
        parts = [
            "Зов к приключению",
            "Отказ от пути",
            "Наставник",
            "Испытания",
            "Кульминация",
            "Возвращение"
        ]

        chars = ", ".join([c.name for c in characters])
        return f"Жанр: {genre}. Герои: {chars}. Структура: {', '.join(parts)}"

    def generate_story(self, db: Session, user_id: int, data):
        prompt = self.build_prompt(data.genre, data.characters)
        text = self.llm.generate_text(prompt)

        story = Story(
            title=data.title,
            content=text,
            user_id=user_id
        )

        db.add(story)
        db.commit()
        db.refresh(story)

        return story