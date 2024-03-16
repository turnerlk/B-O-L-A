
from django.shortcuts import render
from users.middleware.custom_middleware import auth_middleware
from django.http import HttpResponseRedirect


def index_view(request):
    if request.method == "GET":
        return render(request, 'index.html')


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')


def register_view(request):
    if request.method == "GET":
        return render(request, 'register.html')



def dashboard_view(request):

    def dummy_get_response(request):
        pass

    middleware = auth_middleware(dummy_get_response)

    # Executando a middleware
    response = middleware(request)

    if isinstance(response, HttpResponseRedirect):
        return response
    
    return render(request, 'dashboard.html')

def profile_view(request):

    def dummy_get_response(request):
        pass

    middleware = auth_middleware(dummy_get_response)

    # Executando a middleware
    response = middleware(request)

    if isinstance(response, HttpResponseRedirect):
        return response
    
    return render(request, 'profile.html')