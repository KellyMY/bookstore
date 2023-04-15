import pytest
from order.factories import UserFactory

@pytest.fixture
def post_user():
    return UserFactory(email='email@email.com.br')

@pytest.mark.django_db
def test_create_post(post_user):
    assert post_user.email == 'email@email.com.br'