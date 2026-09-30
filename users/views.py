from django.shortcuts import render
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.core.mail import send_mail
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from .forms import UserEdit
# Create your views here.

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_mail(user.email)
        return super().form_valid(form)


    def send_welcome_mail(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:home')
    form_class = CustomAuthenticationForm

class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserEdit
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user