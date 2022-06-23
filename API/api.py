import json
import requests
from settings import head


class PetStore:
    """API-library for Pet Store web application"""
    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/'

    def get_api_login(self, email: str, password: str) -> json:
        """Method makes a request to the server API and returns status of the request and result in JSON format
         with unique key of the user
        :param email: valid user's email
        :param password: valid user's password
        :return: status - request's status code, result -  request's json/text answer
        """
        data = {'username': email,
                'password': password}
        res = requests.get(self.base_url + 'v2/user/login', params=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_api_add_user(self, user_data: str) -> json:
        """Method makes a request to the server API and returns status of the request and result in JSON format
        :param user_data: string user's data in format:
        {
            "id": integer,
            "username": "string",
            "firstName": "string",
            "lastName": "string",
            "email": "string",
            "password": "string",
            "phone": "string",
            "userStatus": integer
        }
        :return: status - request's status code, result -  request's json/text answer
        """

        res = requests.post(self.base_url + 'v2/user', headers=head,
                            data=user_data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def put_api_update_user_name(self, user_name: str, user_data: str) -> json:
        """Method makes a request to the server API and returns status of the request and result in JSON format
        :param user_name: existing user's name
        :param user_data: new user's data
        :return: status - request's status code, result -  request's json/text answer
        """

        res = requests.put(self.base_url+'v2/user' + f'/{user_name}', headers=head, data=user_data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_api_find_user_by_name(self, user_name: str) -> json:
        """Method makes a request to the server API and returns status of the request and result in JSON format
        :param user_name: existing user's name
        :return: status - request's status code, result -  request's json/text answer
        """

        res = requests.get(self.base_url+'v2/user' + f'/{user_name}', headers=head)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def api_delete_user_by_name(self, user_name: str) -> json:
        """Method makes a request to the server API and returns status of the request and result in JSON format
        :param user_name: existing user's name
        :return: status - request's status code, result -  request's json/text answer
        """

        res = requests.delete(self.base_url+'v2/user' + f'/{user_name}', headers=head)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def post_api_add_new_pet(self, pet_object: str) -> json:
        """Method makes a request to the server API and returns status of the request and result in JSON format
        :param pet_object: data that needs to be added to the store in format:
        {
        "id": integer,
        "category": {
            "id": integer,
            "name": "string" },
        "name": "doggie",
        "photoUrls": [ "string" ],
        "tags": [
            { "id": 0,
            "name": "string"
            }
             ],
        "status": "available"
        }
        :return: status - request's status code, result -  request's json/text answer
        """

        res = requests.post(self.base_url + 'v2/pet', headers=head, data=pet_object)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_api_find_pet_by_id(self, pet_id: str) -> json:
        """Method makes a request to the server API and returns status of the request and result in JSON format
        :param pet_id: existing pet's id
        :return: status - request's status code, result -  request's json/text answer
        """

        res = requests.get(self.base_url+'v2/pet' + f'/{pet_id}', headers=head)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
