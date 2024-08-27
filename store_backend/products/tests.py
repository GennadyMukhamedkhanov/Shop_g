# from django.test import TestCase
# from rest_framework.test import APITestCase, APIRequestFactory
#
# class TestListProducts(APIRequestFactory):
#     def test_index(self):
#         # response = self.client.get('/api/list_products/')
#         # cont = response.content.decode()
#         # self.assertEquals(response.status_code, 200)
#         factory = APIRequestFactory()
#         request = factory.get('/api/list_products/')
#         d=4
from pprint import pprint
from rest_framework.test import force_authenticate
from nose.tools import assert_true
import requests
from nose.tools import assert_is_not_none
from users.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from products.models.manufacturers import Manufacturer
from products.models.products import Product
from products.models.warehouse import Warehouse
from products.serializers.products import ListProductsSerializers


class ProductTests(APITestCase):

    def setUp(self):
        manufacturer = Manufacturer.objects.create(
            name='Название компании',
            description='Описание'
        )

        warehous = Warehouse.objects.create(
            name='Vasia',
            amount=77777,
            measurement_unit='JJJJJJJJJJJJJJJ',
            manufacturer=manufacturer
        )

        self.one_product = Product.objects.create(
            name=warehous,
            cost_product=25,
            measurement_unit='kg',
            description='Описание',
            image=None

        )

        self.two_product = Product.objects.create(
            name=warehous,
            cost_product=11,
            measurement_unit='g',
            description='Описание2',
            image=None

        )

        self.user = User.objects.create_user(username='Gena', password='123', phone='9773333333')
        self.user_token = Token.objects.create(user=self.user)

    def test_products_list(self):
        response = self.client.get('/api/list_products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertTrue(
            {
                'name': {'name': 'Vasia', 'amount': 77777,
                         'manufacturer': {'name': 'Название компании', 'description': 'Описание'}},
                'cost_product': 25,
                'measurement_unit': 'kg',
                'description': 'Описание',
                'image': None
            }
            in
            response.json()
        )

    def test_detail_products_db(self):
        product = Product.objects.get(id=self.two_product.id)
        self.assertEqual(product.description, 'Описание2')

    def test_detail_products(self):
        response = self.client.get(reverse('product', kwargs={'id': self.two_product.id}))
        serializers = ListProductsSerializers(self.two_product).data
        self.assertEqual(serializers, response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_me_invalid(self):
        response = self.client.get(reverse('user_me'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_me_valid(self):
        #self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_token.key)
        response = self.client.get(reverse('user_me'), headers={'Authorization': 'Token ' + self.user_token.key})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_me_vaalid(self):
        response = requests.get('http://jsonplaceholder.typicode.com/todos')
        assert_true(response.ok)
