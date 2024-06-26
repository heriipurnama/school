from odoo import models, fields

class ProductSegment(models.Model):
    _name = 'product.segment'
    _description = 'Product Segment'

    name = fields.Char(string='Segment Name', required=True)
