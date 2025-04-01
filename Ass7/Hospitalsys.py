class MedicalRecord:
    def __init__(self, record_id, diagnosis, treatment, medications):
        """
        Kelas untuk merepresentasikan rekam medis pasien.
        Menggunakan composition dengan Patient (rekam medis adalah bagian dari pasien)
        """
        self.record_id = record_id
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.medications = medications
    
    def display_record(self):
        """Menampilkan informasi rekam medis"""
        print(f"Rekam Medis ID: {self.record_id}")
        print(f"Diagnosis: {self.diagnosis}")
        print(f"Perawatan: {self.treatment}")
        print(f"Obat-obatan: {', '.join(self.medications)}")


class Patient:
    def __init__(self, patient_id, name, age, gender):
        """
        Kelas untuk merepresentasikan pasien.
        Menggunakan composition dengan MedicalRecord
        """
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_records = []  # Composition: rekam medis adalah bagian dari pasien
    
    def add_medical_record(self, record_id, diagnosis, treatment, medications):
        """Menambahkan rekam medis baru untuk pasien ini"""
        new_record = MedicalRecord(record_id, diagnosis, treatment, medications)
        self.medical_records.append(new_record)
        print(f"Rekam medis baru ditambahkan untuk pasien {self.name}")
    
    def display_patient_info(self):
        """Menampilkan informasi pasien dan rekam medisnya"""
        print(f"\nInformasi Pasien:")
        print(f"ID: {self.patient_id}")
        print(f"Nama: {self.name}")
        print(f"Umur: {self.age}")
        print(f"Jenis Kelamin: {self.gender}")
        
        print("\nRekam Medis:")
        if not self.medical_records:
            print("Tidak ada rekam medis")
        else:
            for record in self.medical_records:
                record.display_record()
                print("-" * 30)


class Doctor:
    def __init__(self, doctor_id, name, specialization):
        """
        Kelas untuk merepresentasikan dokter.
        Menggunakan aggregation dengan Patient (pasien bisa ada tanpa dokter)
        """
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.patients = []  # Aggregation: pasien bisa ada independen dari dokter
    
    def assign_patient(self, patient):
        """Menambahkan pasien ke daftar pasien dokter ini"""
        self.patients.append(patient)
        print(f"Pasien {patient.name} ditambahkan ke dokter {self.name}")
    
    def remove_patient(self, patient):
        """Menghapus pasien dari daftar pasien dokter ini"""
        if patient in self.patients:
            self.patients.remove(patient)
            print(f"Pasien {patient.name} dihapus dari dokter {self.name}")
        else:
            print(f"Pasien tidak ditemukan dalam daftar dokter {self.name}")
    
    def display_doctor_info(self):
        """Menampilkan informasi dokter dan daftar pasiennya"""
        print(f"\nInformasi Dokter:")
        print(f"ID: {self.doctor_id}")
        print(f"Nama: {self.name}")
        print(f"Spesialisasi: {self.specialization}")
        
        print("\nDaftar Pasien:")
        if not self.patients:
            print("Tidak ada pasien")
        else:
            for patient in self.patients:
                print(f"- {patient.name} (ID: {patient.patient_id})")


class Department:
    def __init__(self, dept_id, name):
        """
        Kelas untuk merepresentasikan departemen rumah sakit.
        Menggunakan composition dengan Doctor (dokter adalah bagian dari departemen)
        """
        self.dept_id = dept_id
        self.name = name
        self.doctors = []  # Composition: dokter adalah bagian dari departemen
    
    def add_doctor(self, doctor):
        """Menambahkan dokter ke departemen ini"""
        self.doctors.append(doctor)
        print(f"Dokter {doctor.name} ditambahkan ke departemen {self.name}")
    
    def remove_doctor(self, doctor):
        """Menghapus dokter dari departemen ini"""
        if doctor in self.doctors:
            self.doctors.remove(doctor)
            print(f"Dokter {doctor.name} dihapus dari departemen {self.name}")
        else:
            print(f"Dokter tidak ditemukan dalam departemen {self.name}")
    
    def display_department_info(self):
        """Menampilkan informasi departemen dan daftar dokternya"""
        print(f"\nInformasi Departemen:")
        print(f"ID: {self.dept_id}")
        print(f"Nama: {self.name}")
        
        print("\nDaftar Dokter:")
        if not self.doctors:
            print("Tidak ada dokter")
        else:
            for doctor in self.doctors:
                print(f"- {doctor.name} (Spesialis: {doctor.specialization})")


class Hospital:
    def __init__(self, name, location):
        """
        Kelas untuk merepresentasikan rumah sakit.
        Menggunakan composition dengan Department (departemen adalah bagian dari rumah sakit)
        """
        self.name = name
        self.location = location
        self.departments = []  # Composition: departemen adalah bagian dari rumah sakit
    
    def add_department(self, department):
        """Menambahkan departemen ke rumah sakit ini"""
        self.departments.append(department)
        print(f"Departemen {department.name} ditambahkan ke rumah sakit {self.name}")
    
    def remove_department(self, department):
        """Menghapus departemen dari rumah sakit ini"""
        if department in self.departments:
            self.departments.remove(department)
            print(f"Departemen {department.name} dihapus dari rumah sakit {self.name}")
        else:
            print(f"Departemen tidak ditemukan dalam rumah sakit {self.name}")
    
    def display_hospital_info(self):
        """Menampilkan informasi rumah sakit dan daftar departemennya"""
        print(f"\nInformasi Rumah Sakit:")
        print(f"Nama: {self.name}")
        print(f"Lokasi: {self.location}")
        
        print("\nDaftar Departemen:")
        if not self.departments:
            print("Tidak ada departemen")
        else:
            for department in self.departments:
                print(f"- {department.name}")


# Contoh penggunaan sistem
if __name__ == "__main__":
    # Membuat rumah sakit
    rs_sentosa = Hospital("Rumah Sakit Sentosa", "Jakarta")
    
    # Membuat departemen
    dept_jantung = Department("D001", "Kardiologi")
    dept_saraf = Department("D002", "Neurologi")
    
    # Menambahkan departemen ke rumah sakit
    rs_sentosa.add_department(dept_jantung)
    rs_sentosa.add_department(dept_saraf)
    
    # Membuat dokter
    dr_smith = Doctor("DOC001", "Dr. Smith", "Kardiolog")
    dr_jones = Doctor("DOC002", "Dr. Jones", "Neurolog")
    
    # Menambahkan dokter ke departemen
    dept_jantung.add_doctor(dr_smith)
    dept_saraf.add_doctor(dr_jones)
    
    # Membuat pasien
    pasien1 = Patient("P001", "Budi", 45, "Laki-laki")
    pasien2 = Patient("P002", "Ani", 32, "Perempuan")
    
    # Menambahkan rekam medis ke pasien
    pasien1.add_medical_record("RM001", "Penyakit Jantung", "Operasi bypass", ["Aspirin", "Statin"])
    pasien2.add_medical_record("RM002", "Migrain Kronis", "Terapi obat", ["Ibuprofen", "Sumatriptan"])
    
    # Menugaskan pasien ke dokter
    dr_smith.assign_patient(pasien1)
    dr_jones.assign_patient(pasien2)
    
    # Menampilkan informasi
    rs_sentosa.display_hospital_info()
    dept_jantung.display_department_info()
    dept_saraf.display_department_info()
    dr_smith.display_doctor_info()
    dr_jones.display_doctor_info()
    pasien1.display_patient_info()
    pasien2.display_patient_info()