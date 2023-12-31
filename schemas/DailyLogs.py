from pydantic import BaseModel
from typing import List


class logs(BaseModel):
    name: str
    datetime: str
    amount: float


class logsresponse(BaseModel):
    lotOfLogs: List[logs]
