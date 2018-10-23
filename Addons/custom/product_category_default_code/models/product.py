# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"
    
    default_code = fields.Char(u'Référence interne')
