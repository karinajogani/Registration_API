from fastapi import APIRouter, status, HTTPException
from db_base.database import SessionLocal
from app.competition.schemas import Competitionpy, CompetitionPy
from app.competition.models import Competition
import datetime

router = APIRouter()
db = SessionLocal()

@router.get('/competitions', status_code=200)
def get_all_competitions():
    competitions = db.query(Competition).all()
    
    return {"data": competitions, "status": 200, "message": "Registration get successfully"}

@router.get('/competitions/{competition_id}', status_code=status.HTTP_200_OK)
def get_an_competition(competition_id: int):
    competition = db.query(Competition).filter(Competition.id == competition_id).first()
    
    return {"data": competition, "status": 200, "message": "Registration retrive successfully"}

@router.post('/competitons', status_code=status.HTTP_201_CREATED)
def create_competiton(payload: Competitionpy):
    
    db_competition = db.query(Competition).filter(Competition.name == payload.name).first()
    
    if db_competition is not None:
        raise HTTPException(status_code=400, detail="Registration already exists")
    
    new_competition = Competition( 
        name=payload.name,
        created_at = datetime.datetime.now(),
        is_delete = False,
        url = payload.url,
        owner_id = CompetitionPy.id 
    )
    
    db.add(new_competition)
    db.commit()
    
    return {"status": 200, "message": "Registration added successfully"}

@router.put('/competitions/{competition_id}', status_code=status.HTTP_200_OK)
def update_an_competition(competition_id: int, competition: Competitionpy):
    
    competition_to_update = db.query(Competition).filter(Competition.id == competition_id).first()
    
    competition_to_update.updated_at = datetime.datetime.now(),

    
    if competition.name != None:
        competition_to_update.name = competition.name
        
    if competition.url != None:
        competition_to_update.url = competition.url
        
    db.commit()
    
    return {"status": 200, "message": "Registration update successfully"}

@router.delete('/competition/{competition_id}')
def delete_competition(competition_id: int):
    competition_to_delete = db.query(Competition).filter(Competition.id == competition_id).first()
    
    if competition_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Registration delete successfully")    
        
    db.delete(competition_to_delete)
    db.commit()

    return {"data": competition_to_delete, "status": 200, "message": "Registration delete successfully"}    
        