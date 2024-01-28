# Web API Controllers

## Description
Simple Web API controller framework for FastAPI

## Example
```python
from fastapi import FastAPI
from webapicontrollers import APIController, Get, Post

class TestController(APIController):

    def __init__(self, app: FastAPI) -> None:
        super().__init__(app)

    @Get('/')
    async def get(self) -> dict:
        return {"method": "GET", "path": "/"}

    @Get('/{arg}')
    async def get_with_arg(self, arg) -> dict:
        return {"method": "GET", "path": "/", "arg": arg}

    @Post('/')
    async def post(self) -> dict:
        return {"method": "POST", "path": "/"}

    @Post('/{arg}')
    async def post_with_arg(self, arg) -> dict:
        return {"method": "POST", "path": "/", "arg": arg}

app = FastAPI()
test_controller = TestController(app)
```
## Caution
This project is in a very early state so far, doesn't do much and might not be very useful to anyone yet. There is no support avilable, use at your own risk