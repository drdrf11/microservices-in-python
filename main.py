"""Application to provide wikipedia information"""

from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wiki_wiki
from mylib.logic import phrase as wiki_phrase

app = FastAPI()


@app.get("/")
async def root():
    """Root for application. User /search or /wiki or /phrase instead"""

    return {"message": "Wikipedia API.  Call /search or /wiki or /phrase"}


@app.get("/search/{value}")
async def search(value: str):
    """Search for page in wikipedia"""

    result = search_wiki(value)
    return {"results": result}


@app.get("/wiki/{value}")
async def wiki(value: str):
    """Retrieve page from wikipedia"""

    result = wiki_wiki(value)
    return {"results": result}


@app.get("/phrase/{value}")
async def phrase(value: str):
    """Retrieve page from wikipedia and return phrases"""

    result = wiki_phrase(value)
    return {"phrases": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
