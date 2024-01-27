from .api import get_token_with_digits,\
                get_sws_id_from_token,\
                get_courses_starting_from_today,\
                send_signature, \
                check_course_code, \
                get_institution_infos, \
                get_courses_between_dates, \
                get_course_details, \
                is_token_valid, \
                get_user_info
                            
from datetime import date, datetime
from .Course import Course

from typing import Any

import sws_wrapper.api as api
api.SIMULATE_REALISTIC_REQUESTS = True

class User:
        
    def __init__(self, token: str) -> None:       
        
        if (not is_token_valid(token)):
            raise ValueError("The provided token is invalid or expired !")
        
        self.token: str = token
        
        self.id: int = get_sws_id_from_token(token)
        
        self.institution: dict[str, Any] = get_institution_infos(token)
        
        user_data: dict[str, Any] = get_user_info(token)
        
        self.first_name: str = user_data['firstName']
        self.last_name: str = user_data['lastName']
        
        self.email: str = user_data['email']
        
        self.reference: str = user_data['reference']
        
    @classmethod  
    def from_digits(cls, institution_code: str, login_code: str, login_pin: str):
        """An auxiliary constructor to get token from institution given digits.

        Args:
            institution_code (str)
            login_code (str)
            login_pin (str)
        """
        token: str = get_token_with_digits(institution_code, login_code, login_pin)['token'] 
        return cls(token)
        
        
    def get_future_courses(self, number_of_courses: int = 4) -> list[Course]:
        
        return list(map(
            lambda json_course: Course(json_course), 
            get_courses_starting_from_today(self.token, number_of_courses)
        ))
    
    def get_todays_courses(self, number_of_courses=5) -> list[Course]:
        
        return list(filter(
            lambda course: course.end.date() == datetime.today().date(),
            self.get_future_courses(number_of_courses)
        ))
        
    def get_courses_between_dates(self, date_from: date, date_to: date) -> list[Course]:
        
        return list(map(
            lambda json_course: Course(json_course), 
            get_courses_between_dates(self.token, date_from, date_to)
        ))
        
    def is_course_signed(self, course: Course) -> bool:
        
        result: dict[str, Any] = get_course_details(self.token, course.id)
        
        return result != {} and result['status'] == "present"
    
    def check_code(self, course: Course, code: str) -> bool:
        
        return check_course_code(self.token, course.id, code)
    
    def get_signature_of_course(self, course: Course) -> str:
        """Gives the url of the signature image for a given course.

        Args:
            course (Course): The course.

        Raises:
            ValueError: If the course is unsigned.

        Returns:
            str: The url of the signature image.
        """
        
        if (not self.is_course_signed(course)):
            raise ValueError("Course not signed")
        
        return get_course_details(self.token, course.id)['url']
        
    def get_current_course(self) -> Course | None:
        """Gives the current course.

        Returns:
            Course | None: The course or nothing.
        """
        
        courses = self.get_todays_courses()
        now = datetime.now().astimezone()
    
        for course in courses:
            if (course.start <= now <= course.end):
                return course
    
    def sign(self, course: Course, image_path: str) -> None:
        
        send_signature(self.token, course.id, image_path, course.place['id'])
        
        
    def __str__(self) -> str:
        return f"User({self.id}: {self.first_name} {self.last_name})"
    
    
    def __repr__(self) -> str:
        return self.__str__()
            