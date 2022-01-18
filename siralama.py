liste= []
tek = []
adet= int(input("Lutfen kac adet sayi girmek istediğinizi belirtin:"))
for x in range(adet):
    sayi= int(input("Lutfen bir tamsayi giriniz:"))
    liste.append(sayi)
    if sayi%2==1:
        tek.append(sayi)
print("Girmis oldugunuz dizi:", liste)
print("Girdiginiz tek sayilarin listesi:",sorted(tek))
print("En buyuk tek sayi:", max(tek))            


