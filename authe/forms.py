from django import forms
from .models import Author

class RegisterForm(forms.ModelForm):
    password = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Author
        fields = ('email', 'username', 'password')


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Author
        fields = ('username', 'password')