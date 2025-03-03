from fastapi import FastAPI

from http import HTTPStatus as HTTPSStatus

from projeto01.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPSStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}
