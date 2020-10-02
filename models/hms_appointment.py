from odoo import models, fields, api, _
from odoo.exceptions import UserError

class HmsAppointment(models.Model):
    _inherit = 'hms.appointment'

    dob = fields.Date(related="patient_id.dob")
    nama_ayah = fields.Char(related="patient_id.nama_ayah")
    nama_ibu = fields.Char(related="patient_id.nama_ibu")

    