from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test


from Ecommerce.forms import RegisterUserForm
from .models import *


def is_admin(user):
    return user.is_authenticated and user.is_staff


def registrazione(request):
    # Creo un istanza del form di registrazione
    form = RegisterUserForm(request.POST)

    if request.method == "POST":
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            # Salvo i dati inseriti nel form
            form.save()

            # Recupero tutti i dati inseriti nel form tramite i nomi dei campi
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('nome')
            last_name = form.cleaned_data.get('cognome')
            telefono = form.cleaned_data.get('cognome')

            # Eseguo l'autenticazione dell'utente con l'username e la password inseriti
            user = authenticate(username=username, password=password)

            # Creo una nuova istanza Utente e la salvo nel DB
            utente = Utente.objects.create(
                username=username, nome=first_name, cognome=last_name, telefono=telefono, email=email, password=password)
            utente.save()
            carrello, created = Carrello.objects.get_or_create(utente=utente)
            messages.success(request, 'Account creato con successo')

    else:
        # Se il metodo di richiesta non dovesse essere "POST" creo un'istanza vuota del form
        form = RegisterUserForm()

    return render(request=request,
                  template_name="./StoreManager/registrazione.html",
                  context={"form": form})


def login_user(request):
    if request.method == "POST":
        # Recupero username e password
        username = request.POST['username']
        password = request.POST['password']

        # Provo ad autenticare l'utente
        user = authenticate(request, username=username, password=password)

        # Se le credenziali sono valide
        if user is not None:
            # Log in dell'utente
            login(request, user)

            response = redirect('prodotti')
            response.set_cookie('username', username)

            return response
        else:
            messages.error(request, 'Login fallito, riprova')
            return render(request, './StoreManager/login.html')
    else:
        return render(request, './StoreManager/login.html')


@login_required(login_url='login')
def prodotti(request):
    # Get del parametro 'tipologia', se non viene fornito di default è una stringa vuota
    tipologia = request.GET.get('tipologia', '')

    # Get del parametro 'prezzo_minimo', se non viene fornito di default è zero
    prezzo_minimo = float(request.GET.get('prezzo_minimo', 0))

    # Get del parametro 'prezzo_massimo', se non viene fornito di default è infinito
    prezzo_massimo = float(request.GET.get('prezzo_massimo', float('inf')))
    print(prezzo_massimo)
    print(prezzo_minimo)
    # Filtra i prodotti in base ai parametri di ricerca

    prodotti = Prodotto.objects.filter(
        prezzo__gte=prezzo_minimo,
        prezzo__lte=prezzo_massimo
    )

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


# View che permette di aggiungere un prodotto al carrello
@login_required(login_url='login')
def aggiungi_al_carrello(request, prodotto_id):
    # Recupero il prodotto scelto tramite il suo id
    prodotto = get_object_or_404(Prodotto, pk=prodotto_id)

    # Recupero l'utente tramite la mail
    utente = get_object_or_404(Utente, email=request.user.email)

    # Ottengo l'istanza del carrello o la creo se non esiste
    carrello, created = Carrello.objects.get_or_create(utente=utente)

    # Ottengo l'istanza di CarrelloProdotto o la creo se non esiste
    carrello_prodotto, prodotto_created = CarrelloProdotto.objects.get_or_create(
        carrello=carrello, prodotto=prodotto, defaults={'quantita': 1})

    # Se il prodotto è già presente nel carrello incremento la quantità
    if not prodotto_created:
        carrello_prodotto.quantita += 1
        carrello_prodotto.save()

    return redirect('carrello')


@login_required(login_url='login')
def rimuovi_dal_carrello(request, prodotto_id):
    # Recupero il prodotto scelto tramite il suo id
    prodotto = get_object_or_404(Prodotto, pk=prodotto_id)

    # Recupero l'utente tramite la mail
    utente = get_object_or_404(Utente, email=request.user.email)

    # Creo/Recupero il carrello dell'utente.
    carrello, created = Carrello.objects.get_or_create(utente=utente)

    carrello_prodotto, prodotto_created = CarrelloProdotto.objects.get_or_create(
        carrello=carrello, prodotto=prodotto, defaults={'quantita': 1})

    # Se il prodotto è già presente nel carrello decremento la quantità
    if not prodotto_created and carrello_prodotto.quantita > 1:
        carrello_prodotto.quantita -= 1
        carrello_prodotto.save()
    else:
        # Se la quantità è 1 allora elimino il prodotto dal carrello
        carrello_prodotto.delete()

    return redirect('carrello')


def checkout(request):
    return render(request, './StoreManager/checkout.html')


@login_required(login_url='login')
def effettua_ordine(request):
    utente = get_object_or_404(Utente, email=request.user.email)
    # Creazione dell'ordine
    ordine = Ordine.objects.create(utente=utente)

    # Recupero del carrello dell'utente con i prodotti
    carrello = Carrello.objects.select_related(
        'utente').prefetch_related('prodotti').get(utente=utente)

    # Associazione degli elementi del carrello all'ordine
    for carrello_prodotto in carrello.carrelloprodotto_set.all():
        carrello_prodotto.ordine = ordine
        carrello_prodotto.save()

    # Calcolo dell'importo totale dell'ordine
    ordine.importo_totale = sum(
        item.prodotto.prezzo * item.quantita for item in ordine.carrelloprodotto_set.all())
    ordine.save()

    # Svuotamento del carrello
    carrello.prodotti.clear()

    messages.success(request, 'Ordine effettuato con successo!')

    return redirect('prodotti')


def is_admin(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(is_admin, login_url='login')
def dashboard(request):
    ordini = Ordine.objects.all()

    # Calcola il totale delle vendite
    total_sales = sum(ordine.importo_totale for ordine in ordini)

    return render(request, './StoreManager/dashboard.html', {'ordini': ordini, 'total_sales': total_sales})


@user_passes_test(is_admin, login_url='login')
def aggiungi_prodotto(request):
    if request.method == "POST":
        nomeProdotto = request.POST['nomeProdotto']
        tipologia = request.POST['tipologia']
        descrizione = request.POST['descrizione']
        quantita = request.POST['quantita']
        prezzo = request.POST['prezzo']

        # Utilizza il metodo create per creare un'istanza di Prodotto
        prodotto = Prodotto.objects.create(
            nome_prodotto=nomeProdotto,
            tipologia=tipologia,
            descrizione=descrizione,
            quantita=quantita,
            prezzo=prezzo
        )

        # Salva l'istanza di Prodotto nel database
        prodotto.save()
        messages.success(request, 'Prodotto aggiunto alla lista!')
    return render(request, "./StoreManager/aggiungiProdotto.html")


@user_passes_test(is_admin, login_url='login')
def modifica_prodotto(request, prodotto_id):
    prodotto = get_object_or_404(Prodotto, pk=prodotto_id)

    # Se il form è stato inviato, processa le modifiche
    if request.method == "POST":
        prodotto.nome_prodotto = request.POST.get('nome_prodotto')
        prodotto.tipologia = request.POST.get('tipologia')
        prodotto.descrizione = request.POST.get('descrizione')
        prodotto.quantita = request.POST.get('quantita')
        prodotto.prezzo = request.POST.get('prezzo')

        prodotto.save()

        messages.success(request, 'Prodotto modificato con successo!')
        return redirect('prodotti')

    return render(request, './StoreManager/modificaProdotto.html', {'prodotto': prodotto})


@user_passes_test(is_admin, login_url='login')
def elimina_prodotto(request, prodotto_id):
    prodotto = get_object_or_404(Prodotto, pk=prodotto_id)

    prodotto.delete()
    messages.success(request, 'Prodotto eliminato con successo!')
    return redirect('prodotti')
