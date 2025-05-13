class ReservasiError(Exception):
    """Kelas dasar untuk semua kesalahan dalam sistem reservasi hotel"""
    def __init__(self, pesan="Terjadi kesalahan pada sistem reservasi"):
        self.pesan = pesan
        super().__init__(self.pesan)

class KamarTidakTersediaError(ReservasiError):
    """Exception yang dilempar ketika kamar yang diminta tidak tersedia"""
    def __init__(self, nomor_kamar, tanggal):
        self.nomor_kamar = nomor_kamar
        self.tanggal = tanggal
        pesan = f"Kamar {nomor_kamar} tidak tersedia pada tanggal {tanggal}"
        super().__init__(pesan)

class PembayaranGagalError(ReservasiError):
    """Exception yang dilempar ketika pembayaran gagal diproses"""
    def __init__(self, id_reservasi, kode_error):
        self.id_reservasi = id_reservasi
        self.kode_error = kode_error
        pesan = f"Pembayaran untuk reservasi {id_reservasi} gagal dengan kode error: {kode_error}"
        super().__init__(pesan)

class TanggalTidakValidError(ReservasiError):
    """Exception yang dilempar ketika tanggal reservasi tidak valid"""
    def __init__(self, tanggal_check_in, tanggal_check_out):
        self.tanggal_check_in = tanggal_check_in
        self.tanggal_check_out = tanggal_check_out
        pesan = f"Tanggal tidak valid: check-in ({tanggal_check_in}) harus sebelum check-out ({tanggal_check_out})"
        super().__init__(pesan)


class Hotel:
    def __init__(self, nama):
        self.nama = nama
        self.kamar_tersedia = {}  
        self.reservasi = {}  
        self.id_reservasi_counter = 1000
    
    def tambah_kamar(self, nomor_kamar, tanggal_tersedia):
        """Menambahkan kamar dengan daftar tanggal tersedia"""
        self.kamar_tersedia[nomor_kamar] = tanggal_tersedia
    
    def cek_ketersediaan(self, nomor_kamar, tanggal):
        """Memeriksa apakah kamar tersedia pada tanggal tertentu"""
        if nomor_kamar not in self.kamar_tersedia:
            return False
        return tanggal in self.kamar_tersedia[nomor_kamar]
    
    def buat_reservasi(self, nama_tamu, nomor_kamar, tanggal_check_in, tanggal_check_out, metode_pembayaran):
        """Membuat reservasi baru"""
        if tanggal_check_in >= tanggal_check_out:
            raise TanggalTidakValidError(tanggal_check_in, tanggal_check_out)
        
        tanggal_menginap = []
        tanggal_saat_ini = tanggal_check_in
        while tanggal_saat_ini < tanggal_check_out:
            tanggal_menginap.append(tanggal_saat_ini)
            tanggal_saat_ini = f"{int(tanggal_saat_ini) + 1}"  
        
        
        for tanggal in tanggal_menginap:
            if not self.cek_ketersediaan(nomor_kamar, tanggal):
                raise KamarTidakTersediaError(nomor_kamar, tanggal)
        
        
        status_pembayaran, kode_error = self.proses_pembayaran(metode_pembayaran)
        if status_pembayaran != "sukses":
            raise PembayaranGagalError(self.id_reservasi_counter, kode_error)
        
        
        id_reservasi = self.id_reservasi_counter
        self.id_reservasi_counter += 1
        
        
        self.reservasi[id_reservasi] = {
            "nama_tamu": nama_tamu,
            "nomor_kamar": nomor_kamar,
            "tanggal_check_in": tanggal_check_in,
            "tanggal_check_out": tanggal_check_out,
            "tanggal_menginap": tanggal_menginap,
            "metode_pembayaran": metode_pembayaran,
            "status": "terkonfirmasi"
        }
        
        
        for tanggal in tanggal_menginap:
            self.kamar_tersedia[nomor_kamar].remove(tanggal)
        
        return id_reservasi
    
    def proses_pembayaran(self, metode_pembayaran):
        """Simulasi proses pembayaran"""
        
        if metode_pembayaran == "kartu_kredit_invalid":
            return "gagal", "CC_DECLINED"
        elif metode_pembayaran == "saldo_kurang":
            return "gagal", "INSUFFICIENT_FUNDS"
        else:
            return "sukses", None
    
    def batalkan_reservasi(self, id_reservasi):
        """Membatalkan reservasi dan mengembalikan ketersediaan kamar"""
        if id_reservasi not in self.reservasi:
            raise ReservasiError(f"Reservasi dengan ID {id_reservasi} tidak ditemukan")
        
        reservasi = self.reservasi[id_reservasi]
        nomor_kamar = reservasi["nomor_kamar"]
        
        
        for tanggal in reservasi["tanggal_menginap"]:
            self.kamar_tersedia[nomor_kamar].append(tanggal)
        
        
        self.reservasi[id_reservasi]["status"] = "dibatalkan"
        
        return True
def demo_sistem_reservasi():
    hotel_pesona = Hotel("Hotel Pesona Indonesia")
    
    
    hotel_pesona.tambah_kamar("101", ["20230501", "20230502", "20230503", "20230504", "20230505"])
    hotel_pesona.tambah_kamar("102", ["20230501", "20230502", "20230503", "20230504", "20230505"])
    hotel_pesona.tambah_kamar("103", ["20230501", "20230502"])
    
    print("=== SISTEM RESERVASI HOTEL PESONA INDONESIA ===")
    
    
    try:
        id_reservasi = hotel_pesona.buat_reservasi(
            "Budi Santoso", 
            "101", 
            "20230501", 
            "20230503", 
            "kartu_kredit"
        )
        print(f"✅ Reservasi berhasil dibuat dengan ID: {id_reservasi}")
        print(f"   Detail: {hotel_pesona.reservasi[id_reservasi]}")
    except ReservasiError as e:
        print(f"❌ Error: {e}")
    
    
    try:
        id_reservasi = hotel_pesona.buat_reservasi(
            "Siti Rahayu", 
            "101", 
            "20230501", 
            "20230504", 
            "kartu_kredit"
        )
        print(f"✅ Reservasi berhasil dibuat dengan ID: {id_reservasi}")
    except KamarTidakTersediaError as e:
        print(f"❌ Error: {e}")
        print(f"   Detail: Kamar {e.nomor_kamar} telah dipesan untuk tanggal {e.tanggal}")
    except ReservasiError as e:
        print(f"❌ Error lainnya: {e}")
    
    
    try:
        id_reservasi = hotel_pesona.buat_reservasi(
            "Siti Rahayu", 
            "102", 
            "20230502", 
            "20230504", 
            "kartu_kredit_invalid"
        )
        print(f"✅ Reservasi berhasil dibuat dengan ID: {id_reservasi}")
    except PembayaranGagalError as e:
        print(f"❌ Error: {e}")
        print(f"   Detail: Kode error pembayaran: {e.kode_error}")
    except ReservasiError as e:
        print(f"❌ Error lainnya: {e}")
    
    
    try:
        id_reservasi = hotel_pesona.buat_reservasi(
            "Ahmad Rizki", 
            "103", 
            "20230503", 
            "20230502", 
            "transfer_bank"
        )
        print(f"✅ Reservasi berhasil dibuat dengan ID: {id_reservasi}")
    except TanggalTidakValidError as e:
        print(f"❌ Error: {e}")
        print(f"   Detail: Check-in ({e.tanggal_check_in}) tidak boleh setelah check-out ({e.tanggal_check_out})")
    except ReservasiError as e:
        print(f"❌ Error lainnya: {e}")

if __name__ == "__main__":
    demo_sistem_reservasi()