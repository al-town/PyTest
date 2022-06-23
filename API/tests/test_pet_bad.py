import pytest
import string
from api import PetStore
from settings import user_data1, user_data2, generate_string

ps = PetStore()


@pytest.mark.parametrize("username", [string.punctuation], ids=['special_symbols'])
@pytest.mark.parametrize("first_name", [string.punctuation], ids=['special_symbols'])
@pytest.mark.parametrize("last_name", [string.punctuation], ids=['special_symbols'])
def test_post_api_bad_add_user(username, first_name, last_name):
    """Create User with bad input"""
    data = f'"id": "12", "username": "{username}", "firstName": "{first_name}", "lastName": "{last_name}", ' \
           f'"email": "HelloKitty@test.com", "password": "123321", "phone": "+7999123456", "userStatus": 0'
    status, result = ps.post_api_add_user("{" + data + "}")
    assert status == 400
    assert 'bad input' in result.get('message')


def test_put_api_bad_update_user_name():
    """Trying to update user with wrong data"""
    data, user_name = user_data1.get('id')
    ps.api_delete_user_by_name(user_name)
    status, result = ps.put_api_update_user_name(user_name, data)
    assert status == 500
    assert 'something bad happened' in result.get('message')


def test_get_api_find_delete_user():
    """Trying to find deleted user by user's name"""
    user_name = user_data2.get('username')
    status, result = ps.get_api_find_user_by_name(user_name)
    assert status == 404
    assert 'User not found' in result.get('message')

