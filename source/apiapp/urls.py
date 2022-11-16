from django.urls import path
from apiapp.views import get_token_view, add_view, subtract_view, multiply_view, divide_view

urlpatterns = [
    path('token', get_token_view, name='token'),
    path('add/', add_view, name='add_view'),
    path('subtract/', subtract_view, name='subtract_view'),
    path('multiply/', multiply_view, name='multiply_view'),
    path('divide/', divide_view, name='divide_view')
]
