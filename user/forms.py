from django import forms
from django.contrib.auth.hashers import check_password
from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=32, label="Username",
                               error_messages={
                                   'required': 'Please type in your username.'
                               })

    password = forms.CharField(widget=forms.PasswordInput, label="Password",
                               error_messages={
                                   'required': 'Please type in your password.'
                               })

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            # Check if username exists in DB
            try:
                user = User.objects.get(username=username)
                #  Check if password matches
                if not check_password(password, user.password):
                    self.add_error('password', 'Incorrect password')
                else:
                    self.user_id = user.id

            except User.DoesNotExist:
                self.add_error('username', 'Unregistered username.')
