from typing import Any
from datetime import datetime

def get_datetime_from_string(string_datetime: str) -> datetime:
    """Parses the time format given by the API to a datetime object.
    
    The format follows this form : "2024-01-19T14:10:33.571Z"

    Args:
        string_datetime (str): The given time by the API.

    Returns:
        datetime: The datetime object resulting.
    """
    return datetime.strptime(string_datetime, "%Y-%m-%d %H:%M:%S%z").astimezone()

class Course:
    def __init__(self, json_course: dict[str, Any]) -> None:
        
        self.id: str = json_course['id']
        self.name: str = json_course['name']
        
        # Just get the important id and name fields.
        if ('place' in json_course.keys()):
            self.place: dict[str, str] = {k:v for (k,v) in json_course['place'].items() if k in 'id name'}
        
        self.start = get_datetime_from_string(f"{json_course['date']} {json_course['start']}")
        self.end = get_datetime_from_string(f"{json_course['date']} {json_course['end']}")

        
    def __str__(self) -> str:
        return f"Course({self.id}: {self.name} --- {self.start.strftime('%d-%m-%Y %H:%M')} - {self.end.strftime('%H:%M')})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, other) -> bool:
        return other is not None and self.id == other.id and self.name == other.name