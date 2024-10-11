import uvicorn
from src.service.service import app

if __name__ == "__main__":
    import uvicorn
    # Running FastAPI on host 0.0.0.0 (accessible in the network) and port 8000
<<<<<<< HEAD
    uvicorn.run(app, host="0.0.0.0", port=1001)
=======
    uvicorn.run(app, host="0.0.0.0", port=8000)
>>>>>>> c0f0a6c5f1a622487a948c9e4f3d4eeaa005de60
