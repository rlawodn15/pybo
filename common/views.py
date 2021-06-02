from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserFrom

def signup(request):
    if request.method == "POST":
        form = UserFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserFrom()
    return render(request, 'common/signup.html', {'form': form})