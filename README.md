Autor : Matija Mišan

#Zadatak 1

Superuser:

username: matija
password: 1234
običan korisnik (login se izvršava na BASE_URL/accounts/login):

username: kenija
password: nairobi1
registracija (izvršava se na BASE_URL/register):

unosi se username
password se unosi dvaput da ga potvrdimo
upravljanje korisnicima (izvršava se na BASE_URL/admin):

sa superuserom se prijavimo i onda imamo mogućnost brisanja, dodavanja ili uređivanja običnih korisnika
admin stranica (izvršava se na BASE_URL/admin-korisnik):

oni koji nisu admin korisnici ispiše im se poruka da nemaju dozvolu za admin stranicu

#Zadatak2

Superuser i običan korisnik ostaju isti, dodane su poveznice i ne treba se više putem URL-a pristupati stranicama, dovoljno je kliknuti na poveznice i otvara se odgovarajuća stranica, omogućena je registracija, prijava i odjava, ako korisnik nije prijavljen ne može pristupiti stranicama, automatski se odjavljuje korisnik kad se ugasi server, omogućeno je filtriranje i prikaz sa ListView te prikaz sa DetailView

#Zadatak3

Implementacija CRUD funkcionalnosti, na početku korisnik se treba ulogirati ili registrirati, zatim ga se preusmjerava na početnu stranicu, ponuđen je izbornik sa linkovima na stranice te se otvaranjem tih stranica nudi pregled, dodavanje, brisanje i ažuriranje podataka.

#Zadatak4

Proširio sam svoju aplikaciju sa RESTful API koristeći Django REST Framework. Pristupa im se sa putem URL-a: BASE_URL/api/igraci . Moguće je dodati novog igrača na dnu stranice klikom na POST kada se ispune polja. Omogućeno je i za natjecanja, timovi, utakmice. Omogućena je i autentifikacija i autorizacija te samo admin korisnik može pristupiti tim stranicama.

ZAVRŠNI ISPIT

Za završni zadatak dodao sam oblikovane okvire za unos i ažuriranje podataka te za pregled pojedinih podataka radi bolje preglednosti. Koristio sam datoteku style.css kako bih uredio stranice na željeni način. Dodao sam pozadinu na početnu stranicu te navigaciju na vrhu svih stranica. Dodao sam tablični način prikaza podataka radi bolje preglednosti te sam linkove zamijenio gumbovima. Dodao sam i 3 testa kroz tests.py koji se mogu izvršiti u terminalu sa naredbom: python3 manage.py test .
