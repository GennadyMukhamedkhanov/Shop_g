from django.urls import path

from products.views.country.list import ListCountry
from products.views.feedback.list_feedback import ListFeedbackView
from products.views.like.get_like import GetProductLikeView, ProductAddLikeView, ProductAddDislikeView
from products.views.products.list_products import ListProductsView, ProductsView
from products.views.shopping_car.add import AddShoppingCarView
from products.views.shopping_car.delete import DelShoppingCarView
from products.views.shopping_car.list import ListShoppingCarView
from products.views.token.create_delete import CreateTokenView, LogoutTokenView
from products.views.users.change_password import ChangePasswordView
from products.views.users.list_create import UserListCreateView
from products.views.users.personal_profile import PersonalProfileView, DataUserView

urlpatterns = [
    path('users/', UserListCreateView.as_view()),
    path('users/me/', PersonalProfileView.as_view(), name='user_me'),
    path('users/<int:id>/', DataUserView.as_view()),
    path('users/change_password/', ChangePasswordView.as_view()),

    path('token/login/', CreateTokenView.as_view()),
    path('token/logout/', LogoutTokenView.as_view()),

    path('list_products/', ListProductsView.as_view(), name='list_products'),
    path('products/<int:id>/', ProductsView.as_view(), name='product'),

    path('list_feedback/', ListFeedbackView.as_view()),

    path('product/<int:id>/like/', GetProductLikeView.as_view()),
    path('product/<int:id>/add_like/', ProductAddLikeView.as_view()),
    path('product/<int:id>/add_dislike/', ProductAddDislikeView.as_view()),

    path('shopping_car_list/', ListShoppingCarView.as_view()),
    path('add_product/<int:id>/shopping_car/', AddShoppingCarView.as_view()),
    path('del_product/<int:id>/shopping_car/', DelShoppingCarView.as_view()),



    path('country/', ListCountry.as_view()),

]



# Todo QQQ 123