from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailEventRegister.as_view()),
    path('', ListEventRegister.as_view()),
    path('create', CreateEventRegister.as_view()),
    path('update/<int:pk>', UpdateEventRegister.as_view()),
    path('delete/<int:pk>', DeleteEventRegister.as_view()),
]
