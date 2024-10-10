from fastapi import FastAPI, Query
from loguru import logger
from src.controller.get_name import GrupName
from src.controller.page_name import PageName

app = FastAPI()

@app.get("/groups_list")
async def groups_list(grup_name: str = Query(...), 
                      cursor: str = Query(None)):
    grup = GrupName()
    try:
        results = await grup.process(grup_name=grup_name, cursor=cursor)
        if results:
            return {"results": results}
        else:
            return {"message": "No data found"}
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return {"message": "Error occurred", "error": str(e)}

@app.get("/page_list")
async def page_list(page_name: str = Query(...), 
                    cursor: str = Query(None)):
    page = PageName()
    try:
        results = await page.process(page_name=page_name, cursor=cursor)
        if results:
            #menampilkan hasil pertama dengan seluruh field (Raw Data)
            return {"results": results}
        else:
            return {"message": "No data found"}
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return {"message": "Error occurred", "error": str(e)}
