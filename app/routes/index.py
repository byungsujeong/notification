from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.database.conn import db
from app.database.schema import Users


router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session),):

    # user = Users(status='active', name="kim")
    # session.add(user)
    # session.commit()

    # Users().create(session, auto_commit=True, name="jeong")

    current_time = datetime.now()

    return Response(f"Notification API (TIME: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")