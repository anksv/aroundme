from django.urls import path
from . import views

urlpatterns = [
    path('savelocations/', views.savelocations),
    path('getlocations/', views.getlocations),
    path('getcurrentlocation/',views.getcurrentlocation),


]