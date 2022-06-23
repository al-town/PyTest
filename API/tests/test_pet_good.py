import pytest
from api import PetStore
from settings import valid_email, valid_password, user_data1, user_data2, pet_data, generate_string

ps = PetStore()


def test_get_api_login():
    """Logs user into the system with valid input data"""
    status, result = ps.get_api_login(valid_email, valid_password)
    assert status == 200
    assert 'logged in' in result.get('message')


@pytest.mark.parametrize("username", ['Cat_girl', generate_string(255), generate_string(1001), ''],
                         ids=['username', '255 symbols', 'more than 1000 symbols', 'empty string'])
@pytest.mark.parametrize("first_name", ['Tonya', generate_string(255), generate_string(1001), ''],
                         ids=['first_name', '255 symbols', 'more than 1000 symbols', 'empty string'])
@pytest.mark.parametrize("last_name", ['Brighton', generate_string(255), generate_string(1001), ''],
                         ids=['last_name', '255 symbols', 'more than 1000 symbols', 'empty string'])
def test_post_api_add_user(username, first_name, last_name):
    """Create User with valid data"""
    data = f'"id": "12", "username": "{username}", "firstName": "{first_name}", "lastName": "{last_name}", ' \
           f'"email": "HelloKitty@test.com", "password": "123321", "phone": "+7999123456", "userStatus": 0'
    status, result = ps.post_api_add_user("{" + data + "}")
    assert status == 200
    assert user_data1.get('id') in result.get('message')


def test_put_api_update_user_name():
    """Update existing user"""
    user_name = user_data1.get('username')
    data = str(user_data2).replace("'", '"')
    status, result = ps.put_api_update_user_name(user_name, data)
    assert status == 200
    assert user_data2.get('id') in result.get('message')


def test_get_api_find_user_by_name():
    """Get user by user's name"""
    user_name = user_data2.get('username')
    status, result = ps.get_api_find_user_by_name(user_name)
    assert status == 200
    assert user_name in result.get('username')


def test_api_delete_user():
    """Delete user by user's name"""
    user_name = user_data2.get('username')
    status, result = ps.api_delete_user_by_name(user_name)
    assert status == 200
    assert user_name in result.get('message')


def test_post_api_add_new_pet():
    """Create a new pet to the store with valid data"""
    data = str(pet_data).replace("'", '"')
    status, result = ps.post_api_add_new_pet(data)
    assert status == 200
    assert pet_data.get('id') == result.get('id')


def test_get_api_find_pet():
    """Get pet by pet's id with valid data"""
    data = str(pet_data).replace("'", '"')
    status_code, result = ps.post_api_add_new_pet(data)
    if status_code == 200:
        id_code = result.get('id')
        status_code, result = ps.get_api_find_pet_by_id(id_code)
        assert pet_data.get('id') == result.get('id')
    else:
        raise Exception("Pet not added")
