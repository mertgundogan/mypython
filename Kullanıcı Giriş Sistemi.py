print("""Kullanıcı Giriş Sistemine Hoş Geldiniz
#######################
(KGS)Kullanıcı Giriş Sistemi
#######################""")
k_adı="mertgundogan"
k_şifre="123456"
star="########################"
while True:
    kullanıcı=input("Lütfen Kayıtlı Olan Kullanıcı Adınızı Giriniz: ")
    şifre=input("Lütfen Şifrenizi Giriniz")

    if (kullanıcı==k_adı) and (şifre==k_şifre):
        print("Sayın",kullanıcı,"Başarıyla Giriş Yaptınız")
        break
    elif (kullanıcı!=k_adı) and (şifre==k_şifre):
        print("Kullanıcı Adı veya Şifrenizi Yanlış Girdiniz!")
        print(star)
    elif (kullanıcı==k_adı) and (şifre!=k_şifre):
        print("Şifrenizi Yanlış Girdiniz!")
        print("Şifrenizi Değiştirmek İster misiniz ? [E/H]")
        cevap=input()
        if cevap=="E" or  cevap=="e":
            yenişifre=input("Lütfen Yeni Şifrenizi Giriniz: ")
            print("Lütfen Bekleyiniz")
            print(star)
            print("Tebrikler Şifreniz Başarıyla Değiştirildi")
            print(star)
            k_şifre=yenişifre
        else:
            print("Tekrar Deneyiniz")
    elif (kullanıcı!=k_adı) and (şifre!=k_şifre):
        print("Kullanıcı Adı veya Şifrenizi Yanlış Girdiniz")
        print(star)
input()
