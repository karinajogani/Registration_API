from fastapi import APIRouter, status, HTTPException
from db_base.database import SessionLocal
from app.competition.schemas import Competitionpy, CompetitionUpdate
from app.competition.models import Competition
import datetime

router = APIRouter()
db = SessionLocal()

@router.get('/competitions', status_code=200)
def get_all_competitions():
    """get method fot get all competitions

    Returns:
        _type_: _description_
    """
    competitions = db.query(Competition).all()

    return {"data": competitions, "status": 200, "message": "Registration get successfully"}

@router.get('/competitions/{competition_id}', status_code=status.HTTP_200_OK)
def get_an_competition(competition_id: str):
    """get method for get particular 1 competition by id

    Args:
        competition_id (str): _description_

    Returns:
        _type_: _description_
    """
    competition = db.query(Competition).filter(Competition.id == competition_id).first()

    return {"data": competition, "status": 200, "message": "Registration retrive successfully"}

@router.post('/competitons', status_code=status.HTTP_201_CREATED)
def create_competiton(payload: Competitionpy):
    """post method for create competition

    Args:
        payload (Competitionpy): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
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

@router.put('/competitions/{competition_id}', status_code=status.HTTP_200_OK)
def update_an_competition(competition_id: str, competition: CompetitionUpdate):
    """put method for update competition

    Args:
        competition_id (str): _description_
        competition (CompetitionUpdate): _description_

    Raises:
        HTTPException: _description_
    """
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

@router.delete('/competition/{competition_id}')
def delete_competition(competition_id: str):
    """delete method for delete competition

    Args:
        competition_id (str): _description_

    Raises:
        HTTPException: _description_

    Returns:
        _type_: _description_
    """
    competition_to_delete = db.query(Competition).filter(Competition.id == competition_id).first()

    if competition_to_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Registration delete successfully")

    db.delete(competition_to_delete)
    db.commit()

    return {"data": competition_to_delete, "status": 200, "message": "Registration delete successfully"}
