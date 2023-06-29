from django.urls import path,include
from rest_framework import routers
from .views import StudentAPI

routers=routers.DefaultRouter()

routers.register(r'StudentAPI',StudentAPI,basename='StudentAPI')

urlpatterns = [
    path('',include(routers.urls))
]
