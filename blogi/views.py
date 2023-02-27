from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Postaus
from django.urls import reverse
# Create your views here.
def postaukset(request):
    postaukset = Postaus.objects.all()
    context = {'postaukset': postaukset}
    return render(request, 'blogi/postauslista.html', context)

def nayta_postaus(request, id):
    postaus = Postaus.objects.get(id=id)
    context = {"postaus": postaus}
    return render(request, 'blogi/postaus.html', context)
    
def uusi_postaus(request):
    if request.method == 'GET':
        return render(request, "blogi/uusi_postaus.html")
        # 1. Lomake näytetään ensimmäistä kertaan
    elif request.method == 'POST':
        # 2. Käyttäjä täytti ja lähetti lomakkeen

        # luodaan lomakkeen tiedot POST-datasta
        otsikko = request.POST['otsikko']
        teksti = request.POST['teksti']
        # Luodaan uusi Postaus objekti     
        postaus = Postaus.objects.create(
            otsikko=otsikko,
            teksti=teksti,
        )
        # Muodostaa URL-osoite luotun Postaus-objektiin
        url = reverse('nayta_postaus', args=(postaus.id,))
        # Palautetaan uudelleenohjaus uudeen Postaus-objektin URL:iin 
        return redirect(url)

    
