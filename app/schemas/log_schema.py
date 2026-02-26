from pydantic import BaseModel

class LogInput(BaseModel):
    cpu: int
    memory: int
    response_time: int
