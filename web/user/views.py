from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from web.user.forms import FormUser, LoginForm


def signin(request):
    if request.user.is_authenticated:
        return redirect(request.GET.get('next', 'dashboard'))

    form = LoginForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        if not user.is_active:
            messages.add_message(request, messages.ERROR, "Invalid login credentials")
            return redirect("login")
        auth.login(request, user)
        return redirect(request.GET.get('next', 'dashboard'))
    if form.non_field_errors():
        messages.add_message(request, messages.ERROR, "Invalid login credentials")
    return render(request, 'signin.html', {'form': form})


def signup(request):
    signup_form = FormUser(request.POST or None)
    if signup_form.is_valid():
        signup_form.save()
        return redirect('login')
    return render(request, 'signup.html', {'form': signup_form})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')