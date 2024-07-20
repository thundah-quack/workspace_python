class GrandMere():
    def __init__(self,prenom):
        self.prenom=prenom

    def __str__(self):
        print ("Prenom:",(str(self.prenom)))

class Mere(GrandMere):
    def __init__(self,prenom,age):
        self.age=age
        GrandMere.__init__(self,prenom)

    def __str__(self):
        print("Prenom :",str(self.prenom),"| "+"Age : ",str(self.age))



class Fille(Mere):
    def __init__(self,prenom,age,nom):
        self.nom=nom
        Mere.__init__(self,prenom,age)

    def __str__(self):
        print("Prenom :",str(self.prenom),"  | Age : ",str(self.age)," | Nom :",str(self.nom))


a=GrandMere("marjo")
b=Mere("mathilde",66)
c=Fille("mylene",22,"beaudouin")

a.__str__()
b.__str__()
c.__str__()

print ("""B is instance Fille, true or false ? -->""",isinstance(b,Fille))


print ("a est une instance de GrandMere = ",(isinstance(a,GrandMere)))
print ("b est une instance de Mere = ",isinstance(b,Mere))
print ("c est une instance de Fille = ",isinstance(c,Fille))
print ("Mere est une sous-clsse de GrandMere = ",issubclass(Mere,GrandMere),"\n")

# Is Instance A
print ("INSTANCE A")
if (isinstance(a,GrandMere)):
    print ("a est une instance de GrandMere")
else:
    print("a n'est pas une instance de GrandMere")

if (isinstance(a,Fille)):
    print ("a est une instance de Fille")
else:
    print("a n'est pas une instance de Fille")

if (isinstance(a,Mere)):
    print ("a est une instance de Mere")
else:
    print("a n'est pas une instance de Mere\n")





# Is Instance B
print ("INSTANCE B")
if (isinstance(a,GrandMere)):
    print ("a est une instance de GrandMere")
else:
    print("a n'est pas une instance de GrandMere")

if (isinstance(a,Fille)):
    print ("a est une instance de Fille")
else:
    print("a n'est pas une instance de Fille")

if (isinstance(a,Mere)):
    print ("a est une instance de Mere")
else:
    print("a n'est pas une instance de Mere\n")



# Is Instance C
print ("INSTANCE C")
if (isinstance(a,GrandMere)):
    print ("a est une instance de GrandMere")
else:
    print("a n'est pas une instance de GrandMere")

if (isinstance(a,Fille)):
    print ("a est une instance de Fille")
else:
    print("a n'est pas une instance de Fille")

if (isinstance(a,Mere)):
    print ("a est une instance de Mere")
else:
    print("a n'est pas une instance de Mere")