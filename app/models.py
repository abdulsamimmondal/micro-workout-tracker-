from sqlalchemy import Column, Integer, String, DateTime
from .database import Base
from datetime import datetime

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    exercise_name = Column(String, nullable=False)
    reps_or_duration = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
