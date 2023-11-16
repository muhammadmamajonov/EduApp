
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http.response import HttpResponse
from .forms import LoginForm
from django.contrib import messages

class UsersLoginView(View):
    template_name = "users/login.html"
    

    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {"form":form})
    

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(form.cleaned_data)
            user = authenticate(email=email, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Email yoki parol xato")
                return redirect('/users/login/')

    def form_invalid(self, form):
        messages.error(self.request, "Username yoki parol xato")
        return self.render_to_response(self.get_context_data(form=form))