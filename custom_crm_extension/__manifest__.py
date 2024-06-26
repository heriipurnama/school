{
    'name': 'Custom CRM Extension',
    'version': '1.0.0',
    'summary': 'Inherit CRM with additional fields and functionalities',
    'author': 'heriipurnama',
    'web': 'http://heriipurnama.rumahinformatika.com/',
    'depends': ['base','crm'],
    'data': [
        'views/crm_lead_views.xml',
        'views/crm_task_views.xml',
        'views/product_segment_views.xml',
        'data/ir_model_access_data.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
