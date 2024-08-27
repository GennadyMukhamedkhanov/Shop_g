from rest_framework.generics import get_object_or_404
from service_objects.fields import ModelField
from service_objects.services import Service
from products.models.feedbacks import Feedback
from django import forms

from products.models.products import Product
from users.models import User


class GetLikeProduktServices(Service):
    id = forms.IntegerField()

    def process(self):
        return get_object_or_404(Product, id=self.cleaned_data['id'])


class AddLikeServices(Service):
    id = forms.IntegerField()
    user = ModelField(User)
    description = forms.CharField(required=False)

    def process(self):
        product_obj = get_object_or_404(Product, id=self.cleaned_data['id'])
        feedback = Feedback.objects.filter(
            client=self.cleaned_data['user'],
            product=product_obj,

        )

        if not feedback.exists():
            Feedback.objects.create(
                client=self.cleaned_data['user'],
                product=product_obj,
                like=True,
                description=self.cleaned_data['description']
            )
        else:
            feedback = feedback.first()
            feedback.like = True
            feedback.description = self.cleaned_data['description']
            feedback.save()

        return True


class AddDislikeServices(Service):
    id = forms.IntegerField()
    user = ModelField(User)
    description = forms.CharField(required=False)

    def process(self):
        product_obj = get_object_or_404(Product, id=self.cleaned_data['id'])
        feedback = Feedback.objects.filter(
            client=self.cleaned_data['user'],
            product=product_obj,

        )

        if not feedback.exists():
            Feedback.objects.create(
                client=self.cleaned_data['user'],
                product=product_obj,
                like=False,
                description=self.cleaned_data['description']
            )
        else:
            feedback = feedback.first()
            feedback.like = False
            feedback.description = self.cleaned_data['description'] if True else feedback.description
            feedback.save()

        return True
