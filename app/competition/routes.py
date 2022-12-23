from fastapi import APIRouter, Depends, status, HTTPException
from app.competition.schemas import Competitionpy, CompetitionUpdate
from app.competition.models import Competition
import datetime
from db_base.database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

"""get method fot get all competitions"""
@router.get('/competitions', status_code=200)
def get_all_competitions(db: Session = Depends(get_db)):

    competitions = db.query(Competition).all()

    return {"data": competitions, "status": 200, "message": "Registration get successfully"}

"""get method for get particular 1 competition by id"""
@router.get('/competitions/{competition_id}', status_code=status.HTTP_200_OK)
def get_an_competition(competition_id: str, db: Session = Depends(get_db)):

    competition = db.query(Competition).filter(Competition.id == competition_id).first()

    return {"data": competition, "status": 200, "message": "Registration retrive successfully"}

"""post method for create competition"""
@router.post('/competitons', status_code=status.HTTP_201_CREATED)
def create_competiton(payload: Competitionpy, db: Session = Depends(get_db)):

    db_competition = db.query(Competition).filter(Competition.name == payload.name).first()

    if db_competition is not None:
        raise HTTPException(status_code=400, detail="Registration already exists")

    new_competition = Competition(
        name=payload.name,
        created_at = datetime.datetime.now(),
        is_delete = False,
        url = payload.url,
        user_id = payload.user_id
    )

    db.add(new_competition)
    db.commit()

    return {"status": 200, "message": "Registration added successfully"}

"""put method for update competition"""
@router.put('/competitions/{competition_id}', status_code=status.HTTP_200_OK)
def update_an_competition(competition_id: str, competition: CompetitionUpdate, db: Session = Depends(get_db)):

    competition_to_update = db.query(Competition).filter(Competition.id == competition_id).first()

    if not competition_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    competition_to_update.updated_at = datetime.datetime.now(),
    competition_update = competition.dict(exclude_unset=True)
    for key, value in competition_update.items():
        setattr(competition_to_update, key, value)

    db.commit()
    return{"status": 200, "message": "Registration update successfully"}
    # if competition.name != None:
    #     competition_to_update.name = competition.name

    # if competition.url != None:
    #     competition_to_update.url = competition.url

    # db.commit()
    # return {"status": 200, "message": "Registration update successfully"}

"""delete method for delete competition"""
@router.delete('/competition/{competition_id}')
def delete_competition(competition_id: str, db: Session = Depends(get_db)):

    competition_to_delete = db.query(Competition).filter(Competition.id == competition_id).first()

    if competition_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Registration delete successfully")

    db.delete(competition_to_delete)
    db.commit()

    return {"data": competition_to_delete, "status": 200, "message": "Registration delete successfully"}
