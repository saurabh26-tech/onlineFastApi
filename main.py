from fastapi import FastAPI, HTTPException
import pyperclip
import clipboard
app = FastAPI()

class Experiments:
    def __init__(self):
        self.experiments = {}
        for id in [1, 2, 5, 8]:
            try:
                with open(f"{id}.txt", "r") as f:
                    self.experiments[id] = f.read()
            except FileNotFoundError:
                self.experiments[id] = ""

    def get_experiment(self, id):
        return self.experiments[id]

@app.get("/")
async def home():
    return "loading online Java compiler...Please Wait"

@app.get("/java-compiler")
async def exp():
    return "load/num Please Wait Loading Compiler"

@app.get("/load/{id}")
async def get_experiment(id: int):
    ex = Experiments()
    if id not in ex.experiments:
        raise HTTPException(status_code=404, detail="Server Timeout")
    
    copy_to_clipboard(ex.get_experiment(id))
    return "! Online Loading Java Compiler : Failed [Server Down]\n Please Try again After sometime "

def copy_to_clipboard(text):
    clipboard.copy(text)
