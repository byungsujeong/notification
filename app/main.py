import uvicorn

from dataclasses import asdict
from fastapi import FastAPI

from app.database.conn import db, Base
from app.common.config import conf
from app.routes import index, auth


def create_app():

    """ Execute App function """

    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)
    Base.metadata.create_all(db.engine)


    """ router definition """

    app.include_router(index.router)
    app.include_router(auth.router, tags=["Authentication"], prefix="/auth")

    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)