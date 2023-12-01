from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


from Ecommerce.forms import RegisterUserForm
from .models import *


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
            context = {'username_cookie': username}
            return response
        else:
            # se c'è un errore nell'autenticazione rimando l'utente al login
            return render(request, './StoreManager/login.html')
    else:
        return render(request, './StoreManager/login.html')


# view temporanea di test
def base(request):
    return render(request, "./StoreManager/base.html")


@login_required(login_url='login')
def prodotti(request):
    prodotti = Prodotto.objects.all()
    return render(request, "./StoreManager/prodotti.html", {"prodotti": prodotti})


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return render(request, './StoreManager/login.html')


@login_required(login_url='login')
def visualizza_carrello(request):
    # Recupera l'utente autenticato
    utente = get_object_or_404(Utente, email=request.user.email)

    # Recupera il carrello dell'utente con i prodotti
    carrello = Carrello.objects.select_related(
        'utente').prefetch_related('prodotti').get(utente=utente)

    # Passa il carrello con i prodotti al template
    return render(request, './StoreManager/carrello.html', {'carrello': carrello})


@login_required(login_url='login')
def aggiungi_al_carrello(request, prodotto_id):
    prodotto = get_object_or_404(Prodotto, pk=prodotto_id)
    utente = get_object_or_404(Utente, email=request.user.email)

    carrello, created = Carrello.objects.get_or_create(utente=utente)

    carrello_prodotto, prodotto_created = CarrelloProdotto.objects.get_or_create(
        carrello=carrello, prodotto=prodotto, defaults={'quantita': 1})

    if not prodotto_created:
        carrello_prodotto.quantita += 1
        carrello_prodotto.save()

    return redirect('carrello')


@login_required(login_url='login')
def rimuovi_dal_carrello(request, prodotto_id):
    prodotto = get_object_or_404(Prodotto, pk=prodotto_id)
    utente = get_object_or_404(Utente, email=request.user.email)

    carrello, created = Carrello.objects.get_or_create(utente=utente)

    carrello_prodotto, prodotto_created = CarrelloProdotto.objects.get_or_create(
        carrello=carrello, prodotto=prodotto, defaults={'quantita': 1})

    if not prodotto_created and carrello_prodotto.quantita > 1:
        carrello_prodotto.quantita -= 1
        carrello_prodotto.save()
    else:
        carrello_prodotto.delete()

    return redirect('carrello')



@login_required(login_url='login')
def checkout(request):
    return response
















