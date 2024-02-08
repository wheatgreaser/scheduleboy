from fastapi import FastAPI, Response
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from fastapi.middleware.cors import CORSMiddleware

class Tasks(BaseModel):
    title: str
    content: str
    time_alloted: str    

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000"
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
    
)


@app.get('/tasks')
async def get_all_tasks():
    cursor.execute("""SELECT * FROM tasklist ORDER BY id DESC LIMIT 5;""")
    tasks = cursor.fetchall()
    return tasks

@app.post('/tasks')
async def post_a_task(task: Tasks):
    cursor.execute("""INSERT INTO tasklist (title, content, time_alloted) VALUES (%s, %s, %s)""", (task.title, task.content, task.time_alloted))
    conn.commit()
    return{"message": f"{task} was posted"}

@app.delete('/task/{id}')
async def remove_task( id: int):
    cursor.execute("""DELETE FROM tasklist WHERE id = (%s)""", (str(id)))
    conn.commit()
    return{"message": f"post with id: {id} has been deleted"}

while(True):
    try:
        conn = psycopg2.connect() # connect your db here
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("connection to database failed")
        print("Error: ", error)

        time.sleep(2)
