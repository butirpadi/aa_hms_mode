from odoo import models, fields, api, _
from odoo.exceptions import UserError

class HmsPatientDisease(models.Model):
    _inherit = 'hms.patient.disease'

    second_disease = fields.Many2one('hms.diseases', ondelete='set null', string='Second Disease')

    