from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator
app = FastAPI()
instrumentator = Instrumentator().instrument(app)

@app.on_event("startup")
async def _startup():
    instrumentator.expose(app, include_in_schema=True, should_gzip=True)



class user_input(BaseModel):
    word: str

@app.post("/count_words")
async def Word(entry: user_input):
    words = entry.word.split()
    worddict = {}
    for i in words:
        if i not in worddict:
            worddict[i] = 1
        else:
            worddict[i] += 1
    return worddict
