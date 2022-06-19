# 2. Scrie o clasa care repr. un Utilizator
# Atr:
#  - nume
#  - prenume
#  - telefon
#  - email
#  - activ - bool

# Meth: 
#  - activate
#  - deactivate
#  - update_email - 1 param
#  - update_phone - 1 param


class User:

    def __init__(self, name, surname, phone_nr, email, activ):
        self.name = name
        self.surname = surname
        self.phone_nr = phone_nr
        self.email = email
        self.activ = activ

    def activate(self): 
        self.activ = True

    def deactivate(self):
        self.activ = False

    def update_email(self, new_email):
        self.email = new_email

    def update_phone(self, new_phone_nr):
        self.phone_nr = new_phone_nr  
                 
