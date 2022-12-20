from fastapi import FastAPI
import uvicorn
from passfast.randompass import router

app = FastAPI()
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run(debug=True, host='0.0.0.0', port=8000, reload=True)