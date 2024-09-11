from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.models import client  # Ensure this import is correct
from backend.api import router as api_router  # Ensure this import is correct

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with the origin of your frontend application
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.on_event("shutdown")
def shutdown_event():
    client.close()

# Include API routes
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Patient API"}
