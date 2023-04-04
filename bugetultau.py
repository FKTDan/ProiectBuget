class Administratori:
    def __init__(self,ID_Adm,Nume,Prenume,email,parola,isAdmin):
        self.ID_Adm = ID_Adm
        self.Nume = Nume
        self.Prenume = Prenume
        self.email = email
        self.parol = parola
        self.isAdmin = isAdmin
        
class Categorii:
    def __init__(self,ID_Categ,Descriere,Cote_Categ,ID_Adm):
        self.ID_Categ = ID_Categ
        self.Descriere = Descriere
        self.Cote_Categ = Cote_Categ
        self.ID_Adm = ID_Adm
        
class Cheltuieli:
    def __init__(self,ID_Chelt,Data_Chelt,Den_Chelt,Val_Chelt,Cote_Chelt,ID_Categ):
        self.ID_Chelt = ID_Chelt
        self.Data_Chelt = Data_Chelt
        self.Den_Chelt = Den_Chelt
        self.Val_Chelt = Val_Chelt
        self.Cote_Chelt = Cote_Chelt
        self.ID_Categ = ID_Categ

class Rezultate:
    def __init__(self,ID_Rez,Den_Rez,Val_Rez,Cote_Dif,ID_Adm):
        self.ID_Rez = ID_Rez
        self.Den_Rez = Den_Rez
        self.Val_Rez = Val_Rez
        self.Cote_Dif = Cote_Dif
