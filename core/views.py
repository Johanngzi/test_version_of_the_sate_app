from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Invalid username or password"
            return render(request, 'login.html', {
                'error': error,
                'hide_navbar': True
            })

    return render(request, 'login.html', {
        'hide_navbar': True
    })

def results_view(request):
    return render(request, 'results.html')


def competitions_view(request):
    return render(request, 'competitions.html')