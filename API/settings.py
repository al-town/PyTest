import random
import string

valid_email = 'al-town@yandex.ru'
valid_password = '123456'
head = {'accept': 'application/json', 'Content-Type': 'application/json'}

user_data1 = {"id": "12", "username": "Cat_girl", "firstName": "Tonya", "lastName": "Brighton",
              "email": "HelloKitty@test.com", "password": "123321",
              "phone": "+7999123456", "userStatus": 0}
user_data2 = {"id": "13", "username": "BirdBoy", "firstName": "Anton", "lastName": "Popov",
              "email": "BirdBoy@test.com", "password": "112233",
              "phone": "+123456789", "userStatus": 0}

pet_data = {"id": 112, "name": "Rei", "photoUrls": ["https://i.ibb.co/HYTSHm4/1.jpg"]}


def generate_string(n):
    st = random.choices(string.ascii_letters, k=n)
    return ''.join(st)


