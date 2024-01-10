#boş todolist

to_do_list = []

#kullanıcı girdilerini listeye ekleme

def add_task(to_do_list):
    task = input("Yapılacak iş: ")
    to_do_list.append(task)
    print("Başarıyla Eklendi!")

#listedeki görevleri görmek

def show_task(to_do_list):
    print("Yapıalacak İşler: ")
    for task in to_do_list:
        print("- " + task)

#listeden görev silmek

def delete_task(to_do_list):
    task = input("Silmek istenen işi giriniz: ")
    if task in to_do_list:
        to_do_list.remove(task)
        print("Başarıyla silindi!")
    else:
        print("Görev bulunamadı!")

while True:
    print("\n To-Do List Uygulaması")
    print("1. Görev Ekle")
    print("2. Görevleri Göster")
    print("3. Görev Sil")
    print("4. Çıkış")

    choice = input("Seçim Yapınız (1/2/3/4): ")

    if choice == "1":
        add_task(to_do_list)
    elif choice == "2":
        show_task(to_do_list)
    elif choice == "3":
        delete_task(to_do_list)
    elif choice == "4":
        print("Çıkış Yapılıyor...")
        break
    else:
        print("Geçersiz Seçim!")