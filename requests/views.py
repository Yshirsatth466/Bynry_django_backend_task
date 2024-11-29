from django.shortcuts import render, get_object_or_404, redirect
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required

@login_required
def request_list(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'requests/request_list.html', {'requests': requests})

@login_required
def request_detail(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk, user=request.user)
    return render(request, 'requests/request_detail.html', {'request': service_request})

@login_required
def submit_request(request):
    if request.method == 'POST':
        type = request.POST['type']
        details = request.POST['details']
        ServiceRequest.objects.create(user=request.user, type=type, details=details)
        return redirect('request_list')
    return render(request, 'requests/request_form.html')
