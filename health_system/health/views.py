from rest_framework import viewsets
from .models import Client, HealthProgram
from .serializers import ClientSerializer, HealthProgramSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class HealthProgramViewSet(viewsets.ModelViewSet):
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, HealthProgram
from .forms import ClientForm

def dashboard(request):
    return render(request, 'dashboard.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_detail.html', {'client': client})

def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})

def program_list(request):
    programs = HealthProgram.objects.all()
    return render(request, 'program_list.html', {'programs': programs})
