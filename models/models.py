# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class aa_hms_mod(models.Model):
#     _name = 'aa_hms_mod.aa_hms_mod'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100