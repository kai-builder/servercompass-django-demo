from django.urls import path
from . import views

urlpatterns = [
    path('env/', views.get_public_env_vars, name='public_env_vars'),
    path('health/', views.health_check, name='health_check'),
]
