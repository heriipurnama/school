{
    'name': 'Addons Sekolah',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage School',
    'description': """
        Module to manage school
    """,
    'author': 'heriipurnama',
    'web': 'http://heriipurnama.rumahinformatika.com/',
    'depends': ['base'],
    'data': [
        'views/siswa_views.xml',
        'views/kelas_views.xml',
        'views/mata_pelajaran_views.xml',
        'views/jadwal_views.xml',
        'views/guru_views.xml',
        'views/sekolah_menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
