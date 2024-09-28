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
