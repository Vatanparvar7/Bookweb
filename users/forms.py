from django import forms
from .models import CustomUser,ChatModel



class ChatFormm(forms.ModelForm):
    chat=forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'class': 'input-chat',
            'placeholder': 'Xabar yozing!',

        }))
    class Meta:
        model=ChatModel
        fields=('chat',)


class UserRegisterFrom(forms.ModelForm):
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={
        'placeholder':"Enter your username",

        }))
    last_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'placeholder':"Enter your lastname",
        }))
    first_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'placeholder':"Enter your firstname",

        }))
    email = forms.CharField(label="", widget=forms.EmailInput(
        attrs={
            'placeholder':"Enter your email",

        }))
    password = forms.CharField(label="", widget=forms.PasswordInput(
        attrs={
            'class': 'password',
            'placeholder':"Enter your password",

        }))

    class Meta:
        model=CustomUser
        fields=('username','last_name','first_name','email','image','password')

    def save(self, commit=True):
        user=super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return  user

class UserUpdateFrom(forms.ModelForm):
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={
        'placeholder':"Enter your username",

        }))
    last_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'placeholder':"Enter your lastname",
        }))
    first_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={
            'placeholder':"Enter your firstname",

        }))
    email = forms.CharField(label="", widget=forms.EmailInput(
        attrs={
            'placeholder':"Enter your email",

        }))

    class Meta:
        model=CustomUser
        fields=('username','last_name','first_name','email','image',)
