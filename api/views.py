from django.http import JsonResponse
from django.shortcuts import render
from decouple import config


def home(request):
    """
    Homepage that displays public environment variables
    """
    public_vars = {
        'NEXT_PUBLIC_APP_NAME': config('NEXT_PUBLIC_APP_NAME', default=''),
        'NEXT_PUBLIC_API_URL': config('NEXT_PUBLIC_API_URL', default=''),
        'NEXT_PUBLIC_ENVIRONMENT': config('NEXT_PUBLIC_ENVIRONMENT', default=''),
        'NEXT_PUBLIC_VERSION': config('NEXT_PUBLIC_VERSION', default=''),
    }

    return render(request, 'home.html', {'env_vars': public_vars})


def get_public_env_vars(request):
    """
    Returns only public environment variables (those prefixed with NEXT_PUBLIC_)
    to be safely exposed to the frontend.
    """
    public_vars = {
        'NEXT_PUBLIC_APP_NAME': config('NEXT_PUBLIC_APP_NAME', default=''),
        'NEXT_PUBLIC_API_URL': config('NEXT_PUBLIC_API_URL', default=''),
        'NEXT_PUBLIC_ENVIRONMENT': config('NEXT_PUBLIC_ENVIRONMENT', default=''),
        'NEXT_PUBLIC_VERSION': config('NEXT_PUBLIC_VERSION', default=''),
    }

    return JsonResponse(public_vars)


def health_check(request):
    """Simple health check endpoint"""
    return JsonResponse({'status': 'ok', 'message': 'Server Compass API is running'})
