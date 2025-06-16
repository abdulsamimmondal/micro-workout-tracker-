from pydantic import BaseModel
from datetime import datetime

class WorkoutCreate(BaseModel):
    user_name: str
    exercise_name: str
    reps_or_duration: str

class Workout(WorkoutCreate):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
