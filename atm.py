sifre=12345
hesap=7500
kredi_borcu=900
print("Hosgeldiniz")
sayi= int(input("Lutfen sifrenizi giriniz:"))

if sayi==sifre:
            print("Hesap bakiyeniz:", hesap)            
            secim=int(input('''
            Lutfen hangi islemi yapmak istediğiniz seciniz:\n
            para cekmek icin 1\n
            para yatirmak icin 2\n
            kredi karti borcu icin 3\n
            menuden cikmak icin 4
            '''))
            
            if secim==1:
                tutar= int(input("Lutfen cekmek istediginiz tutari giriniz:"))
                hesap= hesap-tutar
            elif secim==2:
                miktar=int(input("Yatirmak istediginiz miktar:"))
                hesap= hesap+miktar
            elif secim==3:
                print("Kredi borcunuz:",kredi_borcu)
                odeme=int(input("Lutfen odemek istedginiz tutari giriniz:"))
                kredi_borcu=kredi_borcu-odeme
                print("Kredi borcunuz:",kredi_borcu)
            elif secim==4:
                print("Tesekkurler, Tekrar bekleriz")
            else:
                print("Gecersiz islem")                                

            print("Hesabinizda kalan tutar:", hesap)
            print("İyi gunler, yine bekleriz")
else: 
    print("Sifre yanlis"'\n'"Tekrar deneyebilirsiniz")        