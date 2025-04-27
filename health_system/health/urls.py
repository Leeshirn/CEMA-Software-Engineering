from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
     ClientViewSet, HealthProgramViewSet
)
from . import views

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'programs', HealthProgramViewSet)

#HTML views 
urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/create/', views.client_create, name='client_create'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('programs/', views.program_list, name='program_list'),
    path('programs/create/', views.program_create, name='program_create'),
    path('clients/<int:pk>/edit/', views.client_edit, name='client_edit'),
    path('login/', views.doctor_login, name='doctor_login'),
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('logout/', views.doctor_logout, name='doctor_logout'),
    path('register/', views.doctor_register, name='doctor_register'),

    #add API routes
    path('api/', include(router.urls)),
]
