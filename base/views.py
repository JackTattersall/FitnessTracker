from django.shortcuts import render


def dashboard(request):
    """Default view for the root"""
    return render(request, 'dashboard.html')
