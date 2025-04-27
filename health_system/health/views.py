from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from .models import Client, HealthProgram, DoctorProfile
from .serializers import ClientSerializer, HealthProgramSerializer
from .forms import ClientForm, HealthProgramForm, DoctorLoginForm, DoctorRegistrationForm


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class HealthProgramViewSet(viewsets.ModelViewSet):
    queryset = HealthProgram.objects.all()
    serializer_class = HealthProgramSerializer

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

@login_required
def client_list(request):
    query = request.GET.get('q')
    if query:
        clients = Client.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

@login_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_detail.html', {'client': client})

@login_required
def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form})

@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form})


@login_required
def program_list(request):
    query = request.GET.get('q')
    
    if query:
        programs = HealthProgram.objects.filter(name__icontains=query)
    else:
        programs = HealthProgram.objects.all()

    # Add a 'client_count' attribute to each program, representing the number of clients
    for program in programs:
        program.client_count = program.clients.count()

    return render(request, 'program_list.html', {'programs': programs})


@login_required
def program_create(request):
    if request.method == 'POST':
        form = HealthProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = HealthProgramForm()
    return render(request, 'program_form.html', {'form': form})


def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            department = request.POST.get('department')
            employee_number = request.POST.get('employee_number')

            DoctorProfile.objects.create(user=user, department=department, employee_number=employee_number)

            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('doctor_dashboard')
        else:
            messages.error(request, 'There was an error during registration.')
    else:
        form = DoctorRegistrationForm()

    return render(request, 'register.html', {'form': form})

def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('doctor_dashboard')  # Redirect to dashboard after login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = DoctorLoginForm()

    return render(request, 'login.html', {'form': form})



def doctor_logout(request):
    logout(request)
    return redirect('home')


@login_required
def doctor_dashboard(request):
    # Get the doctor's profile information
    doctor_profile = DoctorProfile.objects.get(user=request.user)

    return render(request, 'dashboard.html', {'doctor_profile': doctor_profile})
