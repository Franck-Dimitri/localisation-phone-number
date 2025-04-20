# localisation d'un numero de telephone 
# on va utiliser la bibliotheque phonenumbers : qui permet de manipuler les numeros de telephones en python


# import de la bibliotheque
import phonenumbers
# import de la bibliotheque geocoder : qui permet de localiser un phone number (donner son pays)
from phonenumbers import geocoder
from data_number import numero

# on 
ch_numero = phonenumbers.parse(numero, "CH")

# on affiche la localisation avec la focntion description_for_number() ceci en anglais avec l'attibut "en" pour engish
print(geocoder.description_for_number(ch_numero, "en"))

# trouver le service utilise par le numero de telephone

# on importe le module carrier de la bibliotheque phonenumbers :
from phonenumbers import carrier 

# on 
service_numero = phonenumbers.parse(numero, "RO")

# on affiche le nom du service du numero de telephone avec la focntion name_for_number() ceci en anglais avec l'attibut "en" pour engish
print(carrier.name_for_number(service_numero, "en"))


