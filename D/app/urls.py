from django.urls import path
from .views import home, update

urlpatterns = [
    path('', home, name='home'),
    path('update/<int:id>/', update, name='update'),
]
