#program pengecekan berat badan wiam
class _berat():
    def __init__(self, nama, tmpt_lahir, tgl_lahir, gender, berat_badan,):
        self.nama = nama
        self.tmpt_lahir = tmpt_lahir
        self.tgl_lahir = tgl_lahir
        self.gender = gender
        self.berat_badan = berat_badan
        
    def _set (self, nama, tmpt_lahir, tgl_lahir, gender, suhu_tubuh,):
        self.nama = nama
        self.tmpt_lahir = tmpt_lahir
        self.tgl_lahir = tgl_lahir
        self.gender = gender
        self.berat_badan = berat_badan

    def _get (self):
        print('Nama lengkap   : ' + self.nama)
        print('TTL      : ' + self.tmpt_lahir + ', ' +  self.tgl_lahir)
        if self.gender in ['L', 'l']:
            gender = 'Laki-Laki'
        else:
            gender = 'Perempuan'
        print('Gender      :' + gender)

        if self.berat_badan >50:
            print('berat badan normal')
        else:
            if self.berat_badan <39:
                print('berat badan tidak normal')
            else:
                if self.berat_badan ==45:
                    print('berat badan ideal')

print('=============================================')
print('     PROGRAM PENGECEKAN BERAT BADAN    ')
print('=============================================')

nama      = input('Nama lengkap        :')
tmpt_lahir = input('Tempat lahir        :')
tgl_lahir  = input('Tanggal lahir       :')
gender     = input('Gender L/P          :')
berat_badan = float(input('Masukkan berat badan :'))

print('======================================')

proses = _berat(nama,tmpt_lahir,tgl_lahir,gender,berat_badan)
print (proses._get())