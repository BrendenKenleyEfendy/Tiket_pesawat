from os import system
import time
from datetime import datetime

system("cls")
print("Selamat datang, Silahkan masukkan password")
user_password = input("Enter Password :")

while user_password !="12345" :
    print("Pass salah, coba Lagi")
    user_password = input("Enter Password :")
print("WELCOME!!!!")
time.sleep(1)
system("cls")

def menu():
    system("cls")
    menu = """
    ~~~Pesan Tiket~~~
    [A] . Menampilkan Penerbangan dan Kelas
    [B] . Pesan Tiket
    [C] . Pencarian
    [D] . Semua Pesanan
    [E] . Pembatalan
    [F] . Tentang aplikasi
 
    [Q] . KELUAR
        """
    print(menu)
 
def verify_ans(char):
    char = char.upper()
    if char == "Y":
        return True
    else:
        return False
 
def create_id_contact():
    today = datetime.now()
    year = today.year
    month = today.month
    hari = today.day
    counter = len(data_pemesanan)+1
    id_contact = str("%4d%02d%02d-Z%01d" % (year, month, hari, counter))
    return id_contact
 
def pemesanan():
    system("cls")
    print("-Pesan Tiket-")
    nama = input("NAMA\t: ")
    telp = input("TELP\t: ")
    kelas = input("Kelas (Economy/Bussiness/First)\t: ")
    Penerbangan = input("Penerbangan\t: ")
    
    user_ans = input("Apakah anda yakin untuk memesan? (Y/N) : ")
 
    if verify_ans(user_ans):
        id_contact = create_id_contact()
        print("Menyimpan Data ...")
        time.sleep(1)
        data_pemesanan[id_contact] = {
            "nama" : nama,
            "telp" : telp,
            "kelas" : kelas,
            "Penerbangan" : Penerbangan
        }
        print("Pemesanan Berhasil, Silakan Cek Ulang Pesanan untuk Mengetahui Kode pemesanan Anda")
    else:
        print("Pemesanan Gagal, Coba Lagi")
    input("Tekan ENTER untuk kembali ke MENU")
 
def daftar_pesan():
    system("cls")
    daftar = """
        Penerbangan yg tersedia 
    1. Palembang-Surabaya
    2. Surabaya-Papua
    3. Papua-Jakarta
    4. Jakarta-Balikpapan
 
        Kelas
    [A] Economy   : Standard
    [B] Bussiness : Private
    [C] First    : Luxury
 
        """
    print(daftar)
    input("Tekan ENTER untuk kembali ke MENU")
 
def print_data_pemesanan(id_contact = None, all_fields = False, Penerbangan = True):
    if id_contact != None and all_fields == False:
        print(f"""
        -DATA DITEMUKAN-
    Kode \t: {id_contact}
    Nama \t:{data_pemesanan[id_contact]["nama"]}
    Telp \t:{data_pemesanan[id_contact]["telp"]}
    Kelas \t:{data_pemesanan[id_contact]["kelas"]}
    Penerbangan \t:{data_pemesanan[id_contact]["Penerbangan"]}
            """)
    elif id_contact != None and lokasi == False:
        print(f"""
        -DATA DITEMUKAN-
    Kode \t: {id_contact}
    Nama \t:{data_pemesanan[id_contact]["nama"]}
    Telp \t:{data_pemesanan[id_contact]["telp"]}
    Kelas \t:{data_pemesanan[id_contact]["kelas"]}
            """)
    elif all_fields == True:
        for id_contact in data_pemesanan:
            nama = data_pemesanan[id_contact]["nama"]
            telp = data_pemesanan[id_contact]["telp"]
            kelas = data_pemesanan[id_contact]["kelas"]
            Penerbangan = data_pemesanan[id_contact]["Penerbangan"]
            print(f"""
                Kode:{id_contact}
                Nama:{nama}
                Telp:{telp}
                Kelas:{kelas}
                Penerbangan:{Penerbangan}
                """
                )
 
def searching_by_name(file):
    for id_contact in data_pemesanan:
        if data_pemesanan[id_contact]["nama"] == file:
            print_data_pemesanan(id_contact=id_contact)
            return id_contact
    else:
        print("-DATA TIDAK DITEMUKAN-")
        return False
 
def pencarian_pesanan():
    system("cls")
    print("- PENCARIAN PESANAN -")
    nama = input("Pesanan yang ingin dicari : ")
    nama = nama.title()
    result = searching_by_name(nama)
    input("Tekan ENTER untuk kembali ke MENU")
 
def semua_pesanan():
    system("cls")
    print("-SEMUA PESANAN-")
    if len(data_pemesanan) == 0:
        print("BELUM ADA PEMESANAN")
    else:
        print_data_pemesanan(all_fields=True)
    input("Tekan ENTER untuk kembali ke MENU")
 
def Pembatalan():
    system("cls")
    print("-BATAL-")
    nama = input("Pemesanan tiket yang ingin dibatalkan : ")
    nama = nama.title()
    id_contact = searching_by_name(nama)
    result = data_pemesanan[id_contact]
    if result:
        respon = input(f"Yakin ingkin pesanan dibatalkan? (Y/N): ")
        if verify_ans(respon):
            del data_pemesanan[id_contact]
            print("Menyimpan Data ...")
            time.sleep(1)
            print("Pemesanan BERHASIL dibatalkan")
        else:
            print("Pemesanan gagal dibatalkan")
    input("Tekan ENTER untuk kembali ke MENU")

def about():
    print("DIDIRIKAN OLEH SUMINTO sejak tahun 2000")
    input("Tekan ENTER untuk kembali ke MENU")
    
def check_input(char):
    char = char.upper()
    if char == "Q":
        return True
    elif char == "A":
        daftar_pesan()
    elif char == "B":
        pemesanan()
    elif char == "C":
        pencarian_pesanan()
    elif char == "D":
        semua_pesanan()
    elif char == "E":
        Pembatalan()
    elif char == "F":
        about()
        
data_pemesanan = {
    "20201031-F31" : {
        "nama"  : "Jono",
        "telp"  : "085321321324",
        "kelas" : "First",
        "Penerbangan": "Surabaya-Papua"
    },
    "20201023-E51" : {
        "nama" : "Dono",
        "telp" : "0929334738",
        "kelas": "Economy",
        "Penerbangan": "Palembang-Surabaya"
    }
}
stop = False
 
while not stop:
    menu()
    user_input = input("Pilihan : ")
    stop = check_input(user_input)