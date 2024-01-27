# SWS

An API wrapper for the signing application SoWeSign.

It is not for malicious intent.

### The project is still in progress but most of it is functional.

This project is composed of 3 'modules', the basic api, and two classes for easier use.
In most cases you'll just use the `User` class in the `User` module.

## TLDR; Examples

#### Printing the 10 next courses of the given user.
```py
from sws_api_wrapper.User import User

user = User.from_digits(institution_code='0000', login_code='00000000', login_pin='0000')

for course in user.get_future_courses(number_of_courses=10):
    print(course.name, course.start.date())
```

#### Checking if `00000` is the correct code for the 1st course of the day (if it is unsigned).
```py
from sws_api_wrapper.User import User

user = User.from_digits(institution_code='0000', login_code='00000000', login_pin='0000')

course = user.get_todays_courses()[0]
code = '00000'

print(user.check_code(course, code))
```

#### Checking if the 1st course of the day is signed by the user.
```py
from sws_api_wrapper.User import User

user = User.from_digits(institution_code='0000', login_code='00000000', login_pin='0000')

course = user.get_todays_courses()[0]

print(user.is_course_signed(course))
```

#### Getting the url of a signed course
```py
from sws_api_wrapper.User import User

user = User.from_digits(institution_code='0000', login_code='00000000', login_pin='0000')

course = user.get_todays_courses()[0]

print(user.get_signature_of_course(course))
```
