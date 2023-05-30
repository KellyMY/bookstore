import json
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from rest_framework.authtoken.models import Token
from django.urls import reverse

from product.factories import CategoryFactory, ProductFactory
from order.factories import UserFactory, OrderFactory
from product.models import Product
from order.models import Order

class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title='technology')
        self.product = ProductFactory(title='mouse', price=100, category=[self.category])
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        response = self.client.get(
            reverse('order-list', kwargs={'version': 'v1'})
        )

        # print(response)
        # import pdb; pdb.set_trace()
        self.assertSetEqual(response.status_code, status.HTTP_200_OK)
        # import pdb; pdb.set_trace()
        order_data = json.loads(response.content)
        self.assertEqual(order_data['results'][0]['product'][0]['title'], self.product.title)
        self.assertEqual(order_data['results'][0]['product'][0]['price'], self.product.price)
        self.assertEqual(order_data['results'][0]['product'][0]['category'][0]['active'], self.category.active)
        self.assertEqual(order_data['results'][0]['product'][0]['active'], self.product.active)
        self.assertEqual(order_data['results'][0]['product'][0]['category'][0]['title'], self.category.title)
        # order_data = json.loads(response.content)[0]
        # self.assertEqual(order_data['results'][0]['product'][0]['title'], self.product.title)
        # self.assertEqual(order_data['results'][0]['product'][0]['price'], self.product.price)
        # self.assertEqual(order_data['results'][0]['product'][0]['category'][0]['active'], self.category.active)
        # self.assertEqual(order_data['results'][0]['product'][0]['active'], self.product.active)
        # # self.assertEqual(order_data['product'][0]['category'][0]['title'], self.category.title)
        # import pdb; pdb.set_trace()
    def test_create_order(self):
        # import pdb; pdb.set_trace()
        # token = Token.objects.get(user__username=self.user.username)
        # import pdb; pdb.set_trace()
        # self.client.credentials(HTTP_AUTHRIZATION='Token '+token.key)
        user = UserFactory()
        product = ProductFactory()
        category = CategoryFactory()
        # import pdb; pdb.set_trace()
        data = json.dumps({
            'products_id': [product.id],
            # 'product': [product.__dict__],
            # 'product': {'id':product.id,'title': product.title, 'price': product.price},
            # 'product': {product.title},
            # 'product': [product.id,product.price],
    #         'product' : [
    #     {'title': product.title, 'categories_id': [
    #         {'id':'2', 'title': 'fff'}]},
    #  ],
            'user': user.id
        })
        # t = json.dump([product])
        # data_t = json.dumps(t)
        import pdb; pdb.set_trace()
        response = self.client.post(
            reverse('order-list', kwargs={'version': 'v1'}),
            data = data,
            content_type='application/json'
        )

        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_order = Order.objects.get(user=user)