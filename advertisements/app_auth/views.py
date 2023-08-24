from django.shortcuts import render

def profile_view(request):
    return render(request, 'app_auth/profile.html')

def login_view(request):
    return render(request, 'app_auth/login.html')

def logout_view(request):
    return render(request, 'app_auth/login.html')

def register_view(request):
    return render(request, 'app_auth/register.html')



