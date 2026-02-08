import pytest
from http import HTTPStatus
from src.api.users.user_api import UsersApi
import src.api.users.users_data_preparation as user_data_preparation

user_name = 'Dragos'
user_job = 'QA Engineer'

@pytest.fixture
def user_api():
    return UsersApi()

@pytest.fixture
def user_context():
    return {'userid': None}

@pytest.fixture(autouse=True)
def setup_and_teardown(user_api, user_context):
    yield
    if user_context['userid']:
        user_api.delete_user(user_context['userid'])
        print(f'User with the id {user_context["userid"]} was been deleted')


@pytest.mark.parametrize("user_data", [
    {'name': 'Dragos', 'job': 'QA Engineer'},
    {'name': 'Laura', 'job': 'Interpreter'},
])

def test_create_user_should_return_201_when_valid_data_provided(user_data,user_api,user_context):
    #Given
    create_user_data = user_data_preparation.create_user_data(user_data['name'], user_data['job'])
    payload = user_data_preparation.create_user_data_payload(create_user_data)

    # When
    response = user_api.create_user(payload)
    response_json = response.json()
    user_context['userid'] = response_json['id']

    # Then
    assert response_json['name'] == user_data['name']
    assert response_json['job'] == user_data['job']
    assert response.status_code == HTTPStatus.CREATED

def test_create_user_should_return_4xx_when_invalid_data_provided(user_api):
    # Given
    create_user_data_payload = {}

    # When
    response = user_api.create_user(create_user_data_payload)
    response_json = response.json()

    # Then
    assert response_json != {}
    assert response.status_code == HTTPStatus.NOT_FOUND

def test_create_user_should_return_403_when_invalid_API_key_provided():
    # Given
    invalid_user = UsersApi()
    invalid_user.set_api_key('invalid_api_key')

    # When
    create_user_data_payload= user_data_preparation.create_user_data(user_name,user_job)
    response = invalid_user.create_user(create_user_data_payload)
    response_json = response.json()

    # Then
    assert response_json != {}
    assert response.status_code == HTTPStatus.FORBIDDEN

