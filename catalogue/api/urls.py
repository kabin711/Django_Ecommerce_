from django.urls import path
from .views import ProductCreateView

urlpatterns = [
    path('test/', ProductCreateView.as_view(), name='test'),
]