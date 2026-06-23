from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
   return {
       "message": "Hello from FastAPI"
   }
@app.get("/about")
def about():
   return {
       "application": "ISI Housing",
       "version": "1.0"
   }
