from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Ecommerce.forms import RegisterUserForm
from .models import Utente

# Create your views here.


def registrazione(request):
    form = RegisterUserForm(request.POST)
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('nome')
            last_name = form.cleaned_data.get('cognome')
            telefono = form.cleaned_data.get('cognome')

            user = authenticate(username=username, password=password)

            utente = Utente.objects.create(
                username=username, nome=first_name, cognome=last_name, telefono=telefono, email=email, password=password)
            utente.save()
    else:
        form = RegisterUserForm()

    return render(request=request,
                  template_name="./StoreManager/registrazione.html",
                  context={"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Provo ad autenticare l'utente con username e password inseriti
        user = authenticate(request, username=username,
                            password=password)
        if user is not None:
            # Se le credenziali sono presenti nel db allora l'utente viene loggato
            login(request, user)

            # redirect reindirizza l'utente in un'altra pagina
            response = redirect('base')
            response.set_cookie('username', username)

            return response
        else:
            # se c'è un errore nell'autenticazione rimando l'utente al login
            return render(request, './StoreManager/login.html')
    else:
        return render(request, './StoreManager/login.html')


# view temporanea di test
def base(request):
    return render(request, "./StoreManager/base.html")
