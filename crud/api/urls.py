from django.urls import path
from api import views

urlpatterns = [
    path('',views.Registration.as_view()),
    path('rud/<int:pk>/',views.rud.as_view()),
]
