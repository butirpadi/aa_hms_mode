from odoo import models, fields, api, _
from odoo.exceptions import UserError


class HmsPatient(models.Model):
    _inherit = 'hms.patient'

    new_patient_id = fields.Many2one('hms.patient', string='New Patient')

    duplicate_patient_count = fields.Integer(String="Duplicate Patients")
    duplicate_patient_ids = fields.One2many(
        comodel_name='hms.patient',
        inverse_name='new_patient_id',
        string='Detected Same Name Patients',
    )

    @api.onchange('name')
    def onchange_name(self):
        patient_ids = self.env['hms.patient'].search(
            [('name', '=', self.name)])
        self.duplicate_patient_count = len(patient_ids)

        if len(patient_ids) > 0:
            patient_ids = self.env['hms.patient'].search(
                [('name', '=', self.name)])
            self.duplicate_patient_ids = patient_ids.ids
        else:
            self.duplicate_patient_ids = []

    def action_get_duplicacte_patients(self):
        print('Checking duplicate patients')
        patient_ids = self.env['hms.patient'].search(
            [('name', '=', self.name)])
        self.duplicate_patient_ids = patient_ids.ids
