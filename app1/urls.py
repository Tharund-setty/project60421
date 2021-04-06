from django.urls import path
from app1 import views
app_name = 'app1'

urlpatterns = [
    path('',views.sam,name = 'sam'),
    path("<data>/",views.carry_data,name = "carrydata"),
    path("facto/<num>/",views.facto,name = 'facto'),
    path("add/<num1>/<num2>",views.add,name = 'add'),
]
