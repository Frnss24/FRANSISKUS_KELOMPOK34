# Kelas BankAccount (Menggunakan Metode dengan Tipe Return dan Non-return)
class RekeningBank:
    def __init__(self, pemegang_rekening):
        self.pemegang_rekening = pemegang_rekening
        self.saldo = 0  # Saldo awal adalah 0

    # Metode non-return untuk menyetor uang
    def setor(self, jumlah):
        if jumlah > 0:
            self.saldo += jumlah
            print(f"Menyetor Rp{jumlah}. Saldo saat ini adalah Rp{self.saldo}.")
        else:
            print("Jumlah setoran harus lebih dari nol.")

    # Metode non-return untuk menarik uang
    def tarik(self, jumlah):
        if 0 < jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"Menarik Rp{jumlah}. Saldo saat ini adalah Rp{self.saldo}.")
        else:
            print("Saldo tidak mencukupi atau jumlah tidak valid.")
            
# Metode return untuk mengecek saldo
    def cek_saldo(self):
        return f"Saldo rekening untuk {self.pemegang_rekening} adalah Rp{self.saldo}."

def pilih_opsi():
    print("\nOpsi Sistem Bank:")
    print("1. Cek saldo")
    print("2. Setor uang")
    print("3. Tarik uang")
    print("4. Keluar")
    opsi = int(input("Masukkan pilihan Anda (1-4): "))
    return opsi

def kelola_rekening_bank():
    pemegang_rekening = input("Masukkan nama pemegang rekening: ")
    rekening = RekeningBank(pemegang_rekening)  

    while True:  
        opsi = pilih_opsi()  

       
        if opsi == 1:
            saldo = rekening.cek_saldo()  
            print(saldo)
        elif opsi == 2:
            jumlah = float(input("Masukkan jumlah untuk setor: "))
            rekening.setor(jumlah)  
        elif opsi == 3:
            jumlah = float(input("Masukkan jumlah untuk tarik: "))
            rekening.tarik(jumlah)  
        elif opsi == 4:
            print("Terima kasih telah menggunakan layanan kami!")
            break  
        else:
            print("Opsi tidak valid. Silakan coba lagi.")
        if _name_ == "_main_":
            kelola_rekening_bank() 
