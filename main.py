import uvicorn
from src.service.service import app

if __name__ == "__main__":
    import uvicorn
    # Running FastAPI on host 0.0.0.0 (accessible in the network) and port 8000
    uvicorn.run(app, host="0.0.0.0", port=1001)
