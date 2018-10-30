# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"
    
    prospect = fields.Boolean('Est un prospect', default=False)
