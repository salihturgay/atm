import random
def rastgele_isim():
    ilk_isim=["Berk","Kerem","Caner","Burak","Aslı","Ebru","Alara","Cansu"]
    soy_isim=["Sabanci","Korel","Soral","Kargi"]
    return "{} {}" .format(random.choice(ilk_isim),random.choice(soy_isim))
for i in range(5):
    print (rastgele_isim())