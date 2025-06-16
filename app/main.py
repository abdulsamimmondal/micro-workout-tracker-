from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database
from datetime import datetime, date

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/workouts/", response_model=schemas.Workout)
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    db_workout = models.Workout(**workout.dict(), timestamp=datetime.utcnow())
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

@app.get("/workouts/", response_model=list[schemas.Workout])
def get_workouts(db: Session = Depends(get_db)):
    return db.query(models.Workout).all()

@app.get("/workouts/today", response_model=list[schemas.Workout])
def get_today_workouts(db: Session = Depends(get_db)):
    today = date.today()
    return db.query(models.Workout).filter(models.Workout.timestamp >= today).all()

@app.get("/workouts/{workout_id}", response_model=schemas.Workout)
def get_workout(workout_id: int, db: Session = Depends(get_db)):
    workout = db.query(models.Workout).get(workout_id)
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout

@app.delete("/workouts/{workout_id}")
def delete_workout(workout_id: int, db: Session = Depends(get_db)):
    workout = db.query(models.Workout).get(workout_id)
    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")
    db.delete(workout)
    db.commit()
    return {"message": "Deleted successfully"}
