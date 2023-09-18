from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def newlogin(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('challenge_list')  # Redirect to challenges page
            else:
                return render(request, 'user/index.html', {'error': 'Invalid login'})

        elif form_type == 'register':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')  # Redirect to login page

    return render(request, 'user/index.html')
