from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # index
    path('', views.index, name='index'),
    path('post/ajax/spent', views.add_spent, name="add_spent"),
    path('post/ajax/profit', views.add_profit, name="add_profit"),

    path('del/ajax/data/<int:id>', views.remove_data, name="remove"),

    path('post/ajax/type', views.add_dtype, name="add_dtype"),
    path('del/ajax/type/<int:id>', views.remove_dtype, name="remove_dtype"),

    
]
