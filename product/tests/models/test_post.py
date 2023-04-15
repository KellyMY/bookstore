import pytest
from product.factories import ProductFactory

@pytest.fixture
def post_published():
    return ProductFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'