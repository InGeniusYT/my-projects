import phonenumbers
from test import number, number1


from phonenumbers import geocoder

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))


from phonenumbers import carrier

service_number = phonenumbers.parse(number, "RO")

defining_number = ch_number
print(carrier.name_for_number(service_number, "en"))
print(number)
print(defining_number)