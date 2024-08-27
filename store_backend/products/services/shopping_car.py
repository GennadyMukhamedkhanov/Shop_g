from functools import lru_cache

from django import forms
from rest_framework.generics import get_object_or_404
from service_objects.fields import ModelField
from service_objects.services import Service
from products.models.products import Product
from products.models.shopping_car import Shopping_cart
from users.models import User


class AllListShoppingCarService(Service):
    user = ModelField(User)

    def process(self):
        return Shopping_cart.objects.filter(client=self.cleaned_data['user'])


class AddShoppingCarService(Service):
    user = ModelField(User)
    id = forms.IntegerField()
    amount = forms.IntegerField()

    def process(self):
        self.delete_amount_product_for_warehouse()
        self.add_product_in_cart()
        return self.get_shopping_cart()

    def get_shopping_cart(self):
        return Shopping_cart.objects.filter(client=self.cleaned_data['user'])

    @lru_cache
    def get_product(self):
        return get_object_or_404(Product, id=self.cleaned_data['id'])

    def add_product_in_cart(self):
        search_product_in_cart = Shopping_cart.objects.filter(product=self.get_product())
        if not search_product_in_cart.exists():
            Shopping_cart.objects.create(
                client=self.cleaned_data['user'],
                product=self.get_product(),
                amount=self.cleaned_data['amount']
            )
        else:
            obj_cart = search_product_in_cart.first()
            obj_cart.amount += self.cleaned_data['amount']
            obj_cart.save()

    def delete_amount_product_for_warehouse(self):
        warehous = self.get_product().name
        if warehous.amount < self.cleaned_data['amount']:
            raise Exception('This quantity of the product is not in stock')
        warehous.amount -= self.cleaned_data['amount']
        warehous.save()


class DelShoppingCarService(Service):
    user = ModelField(User)
    id = forms.IntegerField()
    amount = forms.IntegerField()

    def process(self):
        self.del_product_in_cart()
        self.add_amount_product_for_warehouse()
        return Shopping_cart.objects.filter(client=self.cleaned_data['user'])

    def del_product_in_cart(self):
        search_product_in_cart = Shopping_cart.objects.filter(product=self.get_product(),
                                                              client=self.cleaned_data['user'])
        if not search_product_in_cart.exists():
            raise Exception('Data is not valid')

        obj_cart = search_product_in_cart.first()
        if self.cleaned_data['amount'] > obj_cart.amount:
            raise Exception('Data is not valid')
        obj_cart.amount -= self.cleaned_data['amount']
        obj_cart.save()
        if obj_cart.amount == 0:
            Shopping_cart.objects.get(product=self.get_product(),
                                      client=self.cleaned_data['user']).delete()

    @lru_cache
    def get_product(self):
        return get_object_or_404(Product, id=self.cleaned_data['id'])

    def add_amount_product_for_warehouse(self):
        warehous = self.get_product().name
        warehous.amount += self.cleaned_data['amount']
        warehous.save()
