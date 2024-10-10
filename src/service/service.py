from fastapi import FastAPI, Query
from src.controller.get_name import GrupName
from src.controller.page_name import PageName

app = FastAPI()

@app.get("/groups_list")
async def groups_list(grup_name: str = Query(..., description="Name of the group to search for")):
    grup = GrupName()
    all_results = []
    
    async for results in grup.process(grup_name=grup_name):  # Memanggil process dengan grup_name
        all_results.extend(results)  # Menggabungkan semua hasil dari pagination

    return {"results": all_results}

@app.get("/page_list")
async def page_list(page_name: str = Query(..., description="Name of the page to search for")):
    results = PageName().get_data(page_name=page_name)  # Memanggil get_data, bukan process
    return results