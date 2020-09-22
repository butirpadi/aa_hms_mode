from odoo import models, fields, api
from datetime import timedelta, datetime
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning


class ACSTreatment(models.Model):
    _inherit = 'hms.treatment'

    second_diagnosis_id = fields.Many2one('hms.diseases', string='Diagnosis 2',
                                          states={'cancel': [('readonly', True)], 'done': [('readonly', True)]})
    patient_appointment_ids = fields.One2many(related='patient_id.appointment_line', string='Patient Appointments')

    @api.model
    def _get_default_physician(self):
        physician = self.env['hms.physician'].search(
            [('user_id', '=', self.env.user.id)])
        if physician:
            return physician.id

    physician_id = fields.Many2one('hms.physician', ondelete='restrict', string='Physician', help='Physician who treated or diagnosed the patient', states={
                                   'cancel': [('readonly', True)], 'done': [('readonly', True)]}, default=_get_default_physician)

    def treatment_running(self):
        result = super().treatment_running()

        # add second desase

        my_disease = self.env['hms.patient.disease'].search(
            [('id', '=', self.patient_disease_id.id)], limit=1)

        my_disease.write({
            'second_disease': self.second_diagnosis_id.id
        })

        return result
