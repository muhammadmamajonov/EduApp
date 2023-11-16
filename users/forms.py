from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, required=True)
    password = forms.CharField(label="Parol", max_length=20, required=True, widget=forms.PasswordInput)

