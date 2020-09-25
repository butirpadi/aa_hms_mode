# -*- coding: utf-8 -*-
{
    'name': "Custom Modul ACS_HMS",

    'summary': """
        custom module for ACS_HMS""",

    'description': """
        custom module for ACS_HMS
    """,

    'author': "haris - 082398371825",
    'website': "https://www.github.com/butirpadi",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'acs_hms', 'acs_hms_hospitalization', 'acs_hms_insurance', 'aa_hms_pengobatan', 'aa_hms_pasien', 'aa_hms_dokter', 'aa_hms_pendaftaran'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hms_treatment_view.xml',
        'views/view_patient_form.xml',
        'views/hms_appointment_view.xml',
        'reports/pasien_penyakit_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}
