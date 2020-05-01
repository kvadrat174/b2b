from django.urls import path
from .views import B2bView, CompanyView, ProductView, OrderView, OrderItemView
app_name = "b2b"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('b2b/', B2bView.as_view()),
    path('company/', CompanyView.as_view()),
    path('product/', ProductView.as_view()),
    path('order/', OrderView.as_view()),
    path('orderitem/', OrderItemView.as_view())
]