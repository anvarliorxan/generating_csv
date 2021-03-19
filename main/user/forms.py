from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(min_length=4, label="Username",
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    password = forms.CharField(min_length=5, required=True, label="Password",
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"}))
