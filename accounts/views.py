from django.shortcuts import render, redirect
from .form import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.




def signup(request):
    signup_form = SignupForm()
    
    if request.method == 'GET':
        return render(request, 'auth/signup.html', {'form':signup_form})
    
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            data = signup_form.cleaned_data
            password = data.get('password')
            signup_form.is_staff = False
            user = signup_form.save(commit= False)
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        return render(request, 'auth/signup.html', {'form':signup_form})
    
    
def user_login(request):
    login_form = LoginForm()

    if request.method == 'GET':
        return render(request, 'auth/login.html', {'form': login_form})

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None and user.is_active and user.is_staff:
            login(request, user)
            return redirect('client:index')
        else:
            return render(request, 'auth/login.html', {'form': login_form, 'error': 'Invalid Credential'})

def user_logout(request):
    logout(request)
    return redirect('accounts:login')
