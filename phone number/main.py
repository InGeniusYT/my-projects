import phonenumbers
from numbers import number_1, number_2


from phonenumbers import geocoder

ch_number = phonenumbers.parse(number_1, "CH")
defining_number = ch_number
print(geocoder.description_for_number(defining_number, "en"))


from phonenumbers import carrier

service_number = phonenumbers.parse(number_1, "RO")

defining_number = ch_number
print(carrier.name_for_number(service_number, "en"))
print(defining_number)
