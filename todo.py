import sys
import json
from datetime import datetime
from colorama import init, Fore, Style
import os

init(autoreset=True)

gorevler = []
dosya_yolu = os.path.join(os.path.dirname(__file__), "gorevler.json")


def gorev_ekle(gorev, oncelik):
    tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    gorevler.append(
        {"gorev": gorev, "tamamlandi": False, "tarih": tarih, "oncelik": oncelik}
    )
    print(Fore.GREEN + f"Görev eklendi: {gorev} - Öncelik: {oncelik}")
    gorevleri_kaydet()


def gorevleri_listele():
    if not gorevler:
        print(Fore.YELLOW + "Görev listesi boş.")
    else:
        for i, gorev in enumerate(gorevler, 1):
            durum = (
                Fore.GREEN + "Tamamlandı"
                if gorev["tamamlandi"]
                else Fore.RED + "Tamamlanmadı"
            )
            print(
                f"{Fore.CYAN}{i}. {Fore.WHITE}{gorev['gorev']} - {durum} - {Fore.BLUE}{gorev['tarih']} - {Fore.MAGENTA}Öncelik: {gorev['oncelik']}"
            )


def gorev_sil(gorev_numarasi):
    if 0 < gorev_numarasi <= len(gorevler):
        silinen_gorev = gorevler.pop(gorev_numarasi - 1)
        print(Fore.GREEN + f"Görev silindi: {silinen_gorev['gorev']}")
        gorevleri_kaydet()
    else:
        print(Fore.RED + "Geçersiz görev numarası.")


def gorev_tamamla(gorev_numarasi):
    if 0 < gorev_numarasi <= len(gorevler):
        gorevler[gorev_numarasi - 1]["tamamlandi"] = True
        gorevler[gorev_numarasi - 1]["tarih"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        print(Fore.GREEN + f"Görev tamamlandı: {gorevler[gorev_numarasi - 1]['gorev']}")
        gorevleri_kaydet()
    else:
        print(Fore.RED + "Geçersiz görev numarası.")


def gorevleri_kaydet():
    with open(dosya_yolu, "w") as dosya:
        json.dump(gorevler, dosya)


def gorevleri_yukle():
    global gorevler
    try:
        with open(dosya_yolu, "r") as dosya:
            gorevler = json.load(dosya)
    except FileNotFoundError:
        gorevler = []


def main():
    gorevleri_yukle()
    while True:
        print(Fore.CYAN + "\nTodo List Uygulaması")
        print(Fore.CYAN + "1. Görev Ekle")
        print(Fore.CYAN + "2. Görevleri Listele")
        print(Fore.CYAN + "3. Görev Sil")
        print(Fore.CYAN + "4. Görev Tamamla")
        print(Fore.CYAN + "5. Çıkış")
        secim = input(Fore.YELLOW + "Seçiminizi yapın: ")

        if secim == "1":
            gorev = input(Fore.YELLOW + "Eklemek istediğiniz görevi yazın: ")
            oncelik = input(Fore.YELLOW + "Görevin öncelik seviyesini yazın (1-5): ")
            gorev_ekle(gorev, oncelik)
        elif secim == "2":
            gorevleri_listele()
        elif secim == "3":
            gorev_numarasi = int(
                input(Fore.YELLOW + "Silmek istediğiniz görev numarasını yazın: ")
            )
            gorev_sil(gorev_numarasi)
        elif secim == "4":
            gorev_numarasi = int(
                input(Fore.YELLOW + "Tamamlamak istediğiniz görev numarasını yazın: ")
            )
            gorev_tamamla(gorev_numarasi)
        elif secim == "5":
            print(Fore.CYAN + "Çıkış yapılıyor...")
            sys.exit()
        else:
            print(Fore.RED + "Geçersiz seçim, lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
