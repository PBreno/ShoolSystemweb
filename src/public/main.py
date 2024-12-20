from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .config.database import get_db
from .views.api import professionalView, addressView, professionView, courseView, subjectView

app = FastAPI(strict_slashes=False)

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(professionalView.router)
app.include_router(addressView.router)
app.include_router(professionView.router)
app.include_router(courseView.router)
app.include_router(subjectView.router)


@app.get("/")
async def root():
    print(get_db())
    return {"message": f"Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
