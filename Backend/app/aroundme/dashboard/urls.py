from django.urls import path
from . import views

urlpatterns = [
    path('saveEmpDetails/', views.saveEmp),
    path('getEmployeeDetail/<int:id>',views.getEmp),
]