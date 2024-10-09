from fastapi import FastAPI, Query
from src.controller.get_name import GrupName
from src.controller.page_name import PageName

app = FastAPI()

@app.get("/groups_list")
async def groups_list(grup_name: str = Query(..., description="Name of the group to search for")):
    results = GrupName().get_data(grup_name=grup_name)  # Memanggil get_data, bukan process
    return results

@app.get("/page_list")
async def page_list(page_name: str = Query(..., description="Name of the page to search for")):
    results = PageName().get_data(page_name=page_name)  # Memanggil get_data, bukan process
    return results