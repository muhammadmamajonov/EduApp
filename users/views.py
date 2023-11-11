
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.http.response import HttpResponse

class UsersLoginView(View):
    # template_name = "users/login.html"

    def get(self, request):
        html = "<form method='post', action='login'><input name='username', type='input'><input name='password', type='password'></form>"
        return render(request, 'users/login.html')

    def form_invalid(self, form):
        messages.error(self.request, "Username yoki parol xato")
        return self.render_to_response(self.get_context_data(form=form))
    

    # def post(self, request):
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')

    #     user = authenticate(email=email, password=password)


def test_view(request):
    return render(request, '/login.html')