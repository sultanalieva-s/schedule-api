import uuid
from enum import Enum

from pydantic import BaseModel, Field


class WeekdayEnum(str, Enum):
    MONDAY = "MON"
    TUESDAY = "TUE"
    WEDNESDAY = "WED"
    THURSDAY = "THU"
    FRIDAY = "FRI"


class Task(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    description: str
    start_day: WeekdayEnum
    end_day: WeekdayEnum
    user_name: str


class TaskIn(BaseModel):
    description: str
    start_day: WeekdayEnum
    end_day: WeekdayEnum
    user_name: str


