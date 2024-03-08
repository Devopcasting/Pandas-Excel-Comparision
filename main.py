from fastapi import FastAPI
from app.routes import route_excel
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory=r"app\static"), name="static")

# Include routes
app.include_router(route_excel.excel_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)