# Django-harjoitus 2023 tammi-maaliskuu

Tässä repositoryssä on Django-harjoitteluprojekti, jota on koodattu
alkuvuodesta 2023.

## Asennus

1. Tee Python-virtuaaliympäristö

   python3 -m venv venv

2. Aktivoi virtuaaliympäristö
   - Voit tehdä tämän VSCodessa, joko vastaamalla Yes kun VSCode kysyy
     että aktivoidaanko virtuaaliympäristö tai jos tätä kysymystä ei
     tule, niin klikkaamalla versionumeroa Python-sanan vierestä
     alapalkista. Python-sana tulee alapalkkiin, kun avaat jonkin
     py-tiedoston (esim. manage.py).
   - Vaihtoehtoisesti voit ajaa Linuxissa `. venv/bin/activate` tai
     Windowsissa `venv\script\activate.ps1`
   - Kun virtuaaliympäristö on aktiivinen, niin terminaalissa lukee
     rivin alussa `(venv)`
3. Asenna tarvittavat Python-paketit

   pip install -r requirements.txt

4. Aja migraatiot tietokantaan:

   python manage.py migrate

   - Tämä luo SQLite-tietokannan `db.sqlite3`-tiedostoon
5. Luo pääkäyttäjä:

   python manage.py createsuperuser
  
   - Käytä käyttäjätunnusta ja salasanaa, jotka muistat helposti.
     Esim. "admin" ja "admin".

## Kehitysympäristön käynnistäminen

Aja Djangon runserver komento:

python manage.py runserver


## Uusien migraatiotiedostojen tekeminen

Kun teet muutoksia models.py-tiedostoon, niin model-muutokset pitää
saada myös tietokantaan.  Tähän käytetään migraatiotiedostoja. Tehtyjen
muutosten pohjalta voi luoda uuden migraatiotiedoston komennolla:

python manage.py makemigrations




{# kommentti #}
{% montrivinen
   kommetti% }
<!--html kommentti
voi olla monirivinen--