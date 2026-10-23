from django.contrib.messages import success
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomUserCreationForm

class UserLoginView(LoginView):
    template_name = "accounts/user_login.html"
    redirect_authenticated_user = True
    next_page = "produtos:produtos_list"



class UserLogoutView(LogoutView):
    next_page = "accounts:login"


class UserCreateView(CreateView):
    template_name = "accounts/user_signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")