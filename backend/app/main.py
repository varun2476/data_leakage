from fastapi import FastAPI

from app.database import Base,engine

from app.routes.auth import router
from app.models.incident import Incident
from app.routes.dashboard import router as dashboard_router
from app.models.employee import Employee
from app.routes.incident import router as incident_router
Base.metadata.create_all(
    bind=engine
)



app=FastAPI(
    title="AI Data Leakage System"
)



app.include_router(router)

app.include_router(incident_router)
app.include_router(dashboard_router)
@app.get("/")
def home():

    return {
        "message":"API Running"
    }