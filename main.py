from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS - Allow all origins for development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage for items
items = []

@app.get("/")
def home():
    return {"message": "Hello from FastAPI - Backend is running!"}

@app.get("/items")
def get_items():
    return {"items": items}

@app.post("/items")
def add_item(item: dict):
    items.append(item)
    return {"message": "Item added successfully", "data": item}