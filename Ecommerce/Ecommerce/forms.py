from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RegisterUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(RegisterUserForm, self).__init__(*args, **kwargs)

    username = forms.CharField(max_length=100, help_text='', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    nome = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    cognome = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    telefono = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}), label='Email', max_length=100)

    password1 = forms.CharField(
        label='Password',
        help_text='<ul><li>La password deve contenere almeno 8 caratteri.</li>'
                  '<li>La password non deve essere troppo simile allo username.</li>'
                  '<li>La password non deve contenere solo numeri.</li>'
                  '<li>La password deve contenere almeno un carattere speciale. </ul>',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Conferma password', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["username", "email", "nome", "cognome",
                  "telefono", "password1", "password2"]
        labels = {
            'nome': _('Nome'),
            'cognome': _('Cognome'),
            'password2': _('Conferma password'),
        }
