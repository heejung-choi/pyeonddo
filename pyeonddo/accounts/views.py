from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET,require_POST,require_safe,require_http_methods
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User


# Create your views here.

@require_http_methods(['GET','POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    context = {'form':form}
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET','POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
           user = form.get_user()
           auth_login(request, user) 
        return redirect('index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request,'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('index')


@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Important!
            messages.success(request, '비밀번호가 성공적으로 변경되었습니다!')
            return redirect('accounts:index', request.user.username)
    else:
        form = PasswordChangeForm(request.user)
        context={
            'form':form,
        }
    return render(request, 'accounts/password.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(
            request.POST, instance=request.user
            )
        if form.is_valid():
            form.save()
            return redirect('accounts:index', request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)


def mypage(request, username):
    if request.user.is_authenticated:
        user_profile = get_object_or_404(get_user_model(),username=username) 
        context ={
            'user_profile': user_profile,
        }
        return render(request,'accounts/mypage.html', context)
    else:
        return redirect('accounts:signup')
