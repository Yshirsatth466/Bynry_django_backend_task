from django.shortcuts import render
from requests.models import ServiceRequest

def dashboard(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'dashboard/dashboard.html', {'requests': requests})
