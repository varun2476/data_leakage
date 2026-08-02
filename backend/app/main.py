from fastapi import FastAPI

from app.routes.admin_alert import router as admin_alert_router
from app.database import Base, engine
from app.routes import scanner
from app.routes.auth import router
from app.routes.dashboard import router as dashboard_router
from app.routes.incident import router as incident_router

from app.models.incident import Incident
from app.models.employee import Employee


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="AI Data Leakage System"
)


app.include_router(router)

app.include_router(
    incident_router
)

app.include_router(
    dashboard_router
)

app.include_router(
    scanner.router
)

app.include_router(
    admin_alert_router
)


@app.get("/")
def home():

    return {
        "message": "API Running"
    }