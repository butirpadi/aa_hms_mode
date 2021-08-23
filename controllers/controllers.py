# -*- coding: utf-8 -*-
from odoo import http

# class AaHmsMod(http.Controller):
#     @http.route('/aa_hms_mode/aa_hms_mode/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aa_hms_mode/aa_hms_mode/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aa_hms_mode.listing', {
#             'root': '/aa_hms_mode/aa_hms_mode',
#             'objects': http.request.env['aa_hms_mode.aa_hms_mode'].search([]),
#         })

#     @http.route('/aa_hms_mode/aa_hms_mode/objects/<model("aa_hms_mode.aa_hms_mode"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aa_hms_mode.object', {
#             'object': obj
#         })