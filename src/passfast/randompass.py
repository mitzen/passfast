import string
import secrets
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()    

class SimplePassword:
    @router.get("/password", tags=["password"])
    async def get(self, passwordLength: int = 20):
        pwdgenerator = RandomPasswordGenerator().generate_password(passwordLength)
        return JSONResponse(pwdgenerator)

class RandomPasswordGenerator:
    def __init__(self) -> None:
        pass

    def generate_password(self, passwordLength : int = 20) -> str:
        return ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(passwordLength))