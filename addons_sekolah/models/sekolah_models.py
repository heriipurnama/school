# File: models/sekolah_models.py
from odoo import models, fields

class Siswa(models.Model):
    _name = 'school.siswa'
    _description = 'Siswa'

    nis = fields.Char(string='NIS', required=True)
    nm_siswa = fields.Char(string='Nama Siswa', required=True)
    jns_kelamin = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Jenis Kelamin')
    tgl_lahir = fields.Date(string='Tanggal Lahir')
    agama = fields.Char(string='Agama')
    nm_ayah = fields.Char(string='Nama Ayah')
    nm_ibu = fields.Char(string='Nama Ibu')
    usia = fields.Integer(string='Usia')
    alamat = fields.Text(string='Alamat')

class Kelas(models.Model):
    _name = 'school.kelas'
    _description = 'Kelas'

    nm_kelas = fields.Char(string='Nama Kelas', required=True)
    nm_siswa_ids = fields.Many2many('school.siswa', string='Nama Siswa')
    wali_kelas = fields.Char(string='Wali Kelas')

class MataPelajaran(models.Model):
    _name = 'school.mata_pelajaran'
    _description = 'Mata Pelajaran'

    nm_mata_pelajaran = fields.Char(string='Nama Mata Pelajaran', required=True)

class Jadwal(models.Model):
    _name = 'school.jadwal'
    _description = 'Jadwal'

    hari = fields.Selection([('senin', 'Senin'), ('selasa', 'Selasa'), ('rabu', 'Rabu'), ('kamis', 'Kamis'), ('jumat', 'Jumat'), ('sabtu', 'Sabtu')], string='Hari', required=True)
    kelas_id = fields.Many2one('school.kelas', string='Kelas', required=True)
    jam = fields.Float(string='Jam', required=True)
    mata_pelajaran_id = fields.Many2one('school.mata_pelajaran', string='Mata Pelajaran', required=True)

class Guru(models.Model):
    _name = 'school.guru'
    _description = 'Guru'

    nip = fields.Char(string='NIP', required=True)
    nm_guru = fields.Char(string='Nama Guru', required=True)
    jns_kelamin = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Jenis Kelamin')
    mata_pelajaran_id = fields.Many2one('school.mata_pelajaran', string='Mata Pelajaran')
    usia = fields.Integer(string='Usia')
    no_telp = fields.Char(string='No. Telp')
    alamat = fields.Text(string='Alamat')
