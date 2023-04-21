
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

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
    



