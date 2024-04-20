#____________________________________________________________________ PROFILES/FORMS.PY
from django import forms
from django_countries.fields import CountryField 
from .models import UserProfile

#_______________________________________________________ UserProfileForm
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'email',
            'country',
        ]

#_______________________________________________________ LoginForm
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


#_______________________________________________________ RegisterForm
class UserRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    country = CountryField().formfield(widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data