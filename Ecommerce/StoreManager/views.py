from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def registrazione(request):
    form = UserCreationForm
    return render(request=request,
                  template_name="./StoreManager/registrazione.html",
                  context={"form": form})


def ciao(request):
    return HttpResponse("ciao")
