from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # index
    path('', views.index, name='index'),
    path('post/ajax/spent', views.add_spent, name="add_spent"),
    path('post/ajax/profit', views.add_profit, name="add_profit")

    
]
