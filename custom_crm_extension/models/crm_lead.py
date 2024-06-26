from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    is_new_customer = fields.Boolean(string='Pelanggan Baru?')
    customer_segment = fields.Selection([
        ('kontruksi', 'Kontruksi'),
        ('perbankan', 'Perbankan'),
        ('pemerintah', 'Pemerintah'),
        ('bumd_bumn', 'BUMD/BUMN'),
        ('kementrian', 'Kementrian'),
        ('swasta_lainnya', 'Swasta Lainnya'),
    ], string='Segment Pelanggan')
    product_segment_id = fields.Many2one('product.segment', string='Segment Product')
    task_ids = fields.One2many('crm.task', 'lead_id', string='Task Progress')
