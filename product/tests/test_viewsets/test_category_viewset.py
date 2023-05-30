import json
from rest_framework.views import status
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

from product.factories import CategoryFactory, ProductFactory
# from order.factories import UserFactory
from product.models import Product, Category
from django.shortcuts import get_object_or_404

class CategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory()

        # self.category = CategoryFactory(
        #     title='technology',
        # )

    def test_get_all_category(self):
        response = self.client.get(
            reverse('category-list', kwargs={'version': 'v1'})
            # reverse('category-list')
        )
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)
        # import pdb; pdb.set_trace()
        self.assertEqual(category_data['results'][0]['title'], self.category.title)

    def test_create_category(self):
        data = json.dumps({
            'title': 'technology',
        })

        response = self.client.post(
            reverse('category-list', kwargs={'version': 'v1'}),
            # reverse('category-list'),
            data=data,
            content_type='application/json'
        )

        # para ver se está funcionando
        # import pdb; pdb.set_trace()
        # coloca o seguinte comando no prompt: poetry run python manage.py test product/tests/test_viewsets

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # created_category = Category.objects.get_or_create(title='tecnhology')
        # created_category = Category.objects.get(title='tecnhology')
        created_category = Category.objects.get(title='technology')
        # created_category = get_object_or_404(Category, title='tecnhology')
        # get_object_or_404()
        # import pdb; pdb.set_trace()


        self.assertEqual(created_category.title, 'technology')