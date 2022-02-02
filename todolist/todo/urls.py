from . import views
from django.urls import path

#this configure in the app, remember to configure in the project also
# the delete url is dinamic<str:pk> because it takes an input
urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete'),
]