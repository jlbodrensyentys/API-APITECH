# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ProductCategory(models.Model):
    _inherit = "product.category"
    
    default_code = fields.Char(u'Référence interne')
    complete_default_code = fields.Char(
        u'Référence interne complète', compute='_compute_complete_default_code',
        store=True)

    @api.depends('default_code', 'parent_id.complete_default_code')
    def _compute_complete_default_code(self):
        for category in self:
            if category.parent_id:
                category.complete_default_code = '%s%s' % (category.parent_id.complete_default_code or '', category.default_code or '')
            else:
                category.complete_default_code = category.default_code or ''
