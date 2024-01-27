# This file is a wrapper of the API in python, it just implements useful functions.

import http.client
import json
from base64 import b64encode, b64decode 
from datetime import date, datetime
import hashlib
from user_agent import generate_navigator

from typing import Any

SO_WE_SIGN = http.client.HTTPSConnection("app.sowesign.com")

SIMULATE_REALISTIC_REQUESTS = False

def __populate_header_with_realistic_content(header: dict[str, Any]) -> dict[str, str]:
    ua = generate_navigator()
    populated = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en",
        "Connection": "keep-alive",
        "Host": "app.sowesign.com",
        "Referer": "https://app.sowesign.com/student/loading",
        "sec-ch-ua": f'"Not A;Brand";v="99", "{ua["app_name"]}";v="{ua["build_version"]}", "{ua["app_code_name"]}";v="{ua["build_version"]}"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": f"{ua['platform']}",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-GPC": "1",
        "User-Agent": f"{ua['user_agent']}"
    }
    populated.update(header)  
    return populated

def __read_and_decode_http_response() -> Any:
    """Just to remove repeated code

    Returns:
        Any: The result of the previous request decoded and loaded by json.
    """
    
    res = SO_WE_SIGN.getresponse()\
                         .read()\
                         .decode("utf-8")
            
    res = json.loads(res) if res != "" else {}
    return res

def __decode_token(token: str) -> dict[str, Any]:
    """Decodes the given token.
    
    The token is encoded in base64.
    We isolate the second part of the token, replace all '-' by '+' and '_' by '/', and decode.

    Args:
        token (str): The token.

    Returns:
        dict: The content of the token.
    """
    
    return json.loads(b64decode(token.split(".")[1].replace("-", "+").replace("_", "/")))


# decode_token = __decode_token

def __encode_token(infos: dict[str, Any]) -> str:
    """Encodes a given dict and creates a token.

    Args:
        infos (dict[str, Any]): The information to encode.
        
        it is this format:
        {
            'aud': 'https://app.sowesign.com',
            'client': {
                'corporateConnector': None,
                'id': 0000,
                'name': 'NAME',
                'sqlVarNumber': None,
                'token': 'M',
                'type': 'standard'
            },
            'entity': {
                'firstName': 'John',
                'id': 0000,
                'lastName': 'Doe',
                'type': 'student'
            },
            'exp': 1111111111, in UNIX time
            'iat': 1111111111, in UNIX time
            'iss': 'https://app.sowesign.com',
            'type': 'student'
        }

    Returns:
        str: The generated token.
    """
    header: dict[str, str] = {'alg': 'HS256', 'typ': 'JWT'}
    
    header_string = b64encode(json.dumps(header).encode()).decode()

    info_string = b64encode(json.dumps(infos).encode()).decode()\
                                                                  .replace("+", "-")\
                                                                  .replace("/", "_")

    return f"{header_string}.{info_string}"
    

def is_token_valid(token: str) -> bool:
    """Checks if a token is SYNTACTICALLY correct. It doesn't check with the server.
    It also checks if the expiration date is valid from the function call.

    Args:
        token (str): The user token

    Returns:
        bool: Is the token SYNTACTICALLY correct
    """
    
    decoded_token: dict[str, Any]
    
    try:
        decoded_token = __decode_token(token)
    except:
        return False
        
    if ('exp' not in decoded_token.keys()):
        return False
        
    if ('entity' not in decoded_token.keys()):
        return False
    
    return datetime.now() < datetime.fromtimestamp(float(decoded_token['exp']))


def get_token_with_digits(institution_code: str, login_code: str, login_pin: str) -> dict[str, Any]:
    """Sends a token request for the given account ids.
    
    SWS sticks all the codes together and encodes it in base64, this constitutes the sent data to get a valid token.

    Args:
        institution_code (str): The institution identifier
        login_code (str): The personal identifier 
        login_pin (str): The personal pin

    Returns:
        tuple[str, str, str]: The response of the API given by this format : 
        {
            token, (The users temporary token of 4h)
            type, (The token type, always 'Bearer')
            refreshToken (The refresh token)
        }
    """
    
    pass_code: str = institution_code + login_code + login_pin
    
    pass_code_encoded: str = b64encode(pass_code.encode()).decode("ascii")
    
    headers = {
        "Authorization": "JBAuth " + pass_code_encoded
    }
    if (SIMULATE_REALISTIC_REQUESTS):
        headers = __populate_header_with_realistic_content(headers)
    
    SO_WE_SIGN.request("POST",
                       "/api/portal/authentication/token",
                       headers=headers,
                       body="") 
    
    return __read_and_decode_http_response()


def get_sws_id_from_token(token: str) -> int:
    return __decode_token(token)["entity"]["id"]


def get_user_info(token: str) -> dict:
    """Gets the servers info of the user.

    Args:
        token (str): The user token

    Returns:
        dict: The API response.
    """
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    if (SIMULATE_REALISTIC_REQUESTS):
        headers = __populate_header_with_realistic_content(headers)
    
    SO_WE_SIGN.request("GET",
                       f"/api/student-portal/students/{get_sws_id_from_token(token)}", 
                       headers=headers)
    
    return __read_and_decode_http_response()
    

def get_server_datetime() -> datetime:
    """Pings the server to know its local time.

    Returns:
        datetime: The servers time.
    """

    SO_WE_SIGN.request("GET",
                       "/api/ping")
    
    res = __read_and_decode_http_response()
    
    server_time = res['time']
    
    return datetime.fromisoformat(server_time).astimezone()
    

def get_courses_starting_from_today(token: str, number_of_courses=4) -> list[dict[str, Any]]:
    """Gets a list of courses assigned to the given token starting from the same day the function is called.

    Args:
        token (str): The user token
        number_of_courses (int, optional): The number of courses to request. Defaults to 4.

    Returns:
        list[dict]: The list of requested courses.
    """
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    if (SIMULATE_REALISTIC_REQUESTS):
        headers = __populate_header_with_realistic_content(headers)
    
    SO_WE_SIGN.request("GET",
                       f"/api/student-portal/future-courses?limit={number_of_courses}", 
                       headers=headers)
    
    return __read_and_decode_http_response()


def get_courses_between_dates(token: str, date_from: date, date_to: date) -> list[dict[str, Any]]:
    """Gets a list of courses between two dates for a given token.

    Args:
        token (str): The user token
        date_from (date): The start date.
        date_to (date): The end date.

    Returns:
        list[dict]: The list of requested courses.
        
        The API response may not contain the ['place'] field.
    """
    
    fmt = "%Y-%m-%d"
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    # if (SIMULATE_REALISTIC_REQUESTS):
    #     headers = __populate_header_with_realistic_content(headers)
    
    SO_WE_SIGN.request("GET", 
                       f"/api/student-portal/courses?from={date_from.strftime(fmt)}&to={date_to.strftime(fmt)}", 
                       headers=headers)
    
    
    return __read_and_decode_http_response()
    

def get_course_details(token: str, course_id: str) -> dict[str, Any]:
    """Get the detail of a course

    Args:
        token (str): The user token
        course_id (str): The id of the course

    Returns:
        dict: If the course is signed it will respond with information, if not the response will be empty.
    """
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    if (SIMULATE_REALISTIC_REQUESTS):
        headers = __populate_header_with_realistic_content(headers)
    
    SO_WE_SIGN.request("GET", 
                       f"/api/student-portal/courses/{course_id}/assiduity", 
                       headers=headers)
        
    return __read_and_decode_http_response()


def check_course_code(token: str, course_id: str, code: str) -> bool:
    """Checks if the given code unlocks the course signature.
    Only works for non signed courses.

    Args:
        token (str): The user token
        course_id (str): The course
        code (str): The code to test

    Returns:
        dict: The response from the API.
    """
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    
    body = {
        "value": code,
        "type": 2
    }
    body = json.dumps(body)
    
    if (SIMULATE_REALISTIC_REQUESTS):
        headers = __populate_header_with_realistic_content(headers)
        

    SO_WE_SIGN.request("POST", 
                       f"/api/student-portal/courses/{course_id}/checkcode", 
                       body=body, headers=headers)
    
    print(x:=__read_and_decode_http_response())
    
    return 'Error' not in x["status"]
    

def send_signature(token: str, course_id: str, png_signature_path: str, place_id: str = "-1") -> None:
    """Sends a signature for a specific course.

    Args:
        token (str): The user token
        course_id (str): The course id
        png_signature_path (str): The path of a png image
        place_id (int, optional): The place id. Defaults to -1.
    """
    
    with open(png_signature_path, 'rb') as image:
        encoded_image: str = "data:image/png;base64," + b64encode(image.read()).decode('ascii')
        
    hashed_encoded_image = hashlib.md5(encoded_image.encode()).hexdigest()
        
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    
    body = {
        "signedOn": f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}+01:00",
        "collectedOn": f"{datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}+01:00",
        "md5": f"{hashed_encoded_image}",
        "status": "present",
        "signer": get_sws_id_from_token(token=token),
        "course": course_id,
        "file": f"{encoded_image}"
    }
    
    if (SIMULATE_REALISTIC_REQUESTS):
        
        headers = __populate_header_with_realistic_content(headers)
        
        assert place_id != "-1", "To simulate, you MUST indicate the place_id"
        
        body.update({
            "place": place_id,
            "campus": None,
            "collectMode": "studentPortal", # or studentApp for simulating phone app
        })
        
    body = json.dumps(body)
    
    SO_WE_SIGN.request("POST", 
                       "/api/student-portal/signatures", 
                       body, 
                       headers)
    

def get_institution_infos(token: str) -> dict[str, Any]:
    """Gets institution code from token.

    Args:
        token (str): The user token.

    Returns:
        dict[str, Any]: The API result.
        
        {
            'address': {
                'city': '',
                'country': '',
                'line1': '',
                'line2': '',
                'line3': '',
                'line4': '',
                'state': '',
                'zipCode': ''
            },
            'app': {
                'bannerUrl': '',
                'logoUrl': ''
            },
            'attendance': {
                'footer1': '',
                'footer2': ''
                'headerLogoUrl': '',
                'mainLogoUrl': '',
                'signerName': '',
                'signerRole': '',
                'signerUrl': ''
            },
            'city': '',
            'dataRegion': '',
            'description': '',
            'id': 1,
            'identificationNumber': '',
            'main': True,
            'managerTab': [
                {
                    'active': True,
                    'email': '',
                    'firstName': '',
                    'id': 1,
                    'lastName': '',
                    'phone': '',
                    'support': False
                }
            ],
            'name': '',
            'organizationName': '',
            'reference': '',
            'registrationNumber': '',
            'signerName': '',
            'updatedBy': '',
            'updatedOn': ''
        }
    """
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    if (SIMULATE_REALISTIC_REQUESTS):
        headers = __populate_header_with_realistic_content(headers)
    
    SO_WE_SIGN.request("GET", 
                       f"/api/student-portal/institutions/main", 
                       headers=headers)
    
    return __read_and_decode_http_response()