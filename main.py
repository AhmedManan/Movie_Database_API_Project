from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Movie Database API. Powered by MananAcademy.com"}

# 127.0.0.1/movies/1?query=api
@app.get("/movies/{movie_id}")
async def get_movie(movie_id: int, query: str = None):
    return {"movie_id": movie_id, "query": query}