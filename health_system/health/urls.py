from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    dashboard, client_list, client_detail,
    client_create, program_list,
    ClientViewSet, HealthProgramViewSet
)

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'programs', HealthProgramViewSet)

#HTML views 
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('dashboard/', dashboard, name='dashboard'),
    path('clients/', client_list, name='client_list'),
    path('clients/create/', client_create, name='client_create'),
    path('clients/<int:pk>/', client_detail, name='client_detail'),
    path('programs/', program_list, name='program_list'),

    #add API routes
    path('api/', include(router.urls)),
]
