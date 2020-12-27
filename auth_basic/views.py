from django.shortcuts import render, redirect, get_object_or_404
from auth_basic.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


def index(request):
    return render(request, 'auth_basic/index.html')


@login_required
def user_dashboard(request):
    return render(request, 'auth_basic/dashboard.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('auth_basic:index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('auth_basic:user_dashboard'))
            else:
                return render(request, 'auth_basic/login.html',
                              {'error': 'Username is not active, please contact administrator.'})
        else:
            print('Someone tried to login and failed.')
            print(f"Username: {username} and password: {password}")
            return render(request, 'auth_basic/login.html',
                          {'error': 'Invalid login details supplied.'})
    else:
        return render(request, 'auth_basic/login.html')


def user_registration(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    }
    return render(request, 'auth_basic/register.html', context)
