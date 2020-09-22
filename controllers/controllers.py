# -*- coding: utf-8 -*-
from odoo import http

# class AaHmsMod(http.Controller):
#     @http.route('/aa_hms_mod/aa_hms_mod/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aa_hms_mod/aa_hms_mod/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('aa_hms_mod.listing', {
#             'root': '/aa_hms_mod/aa_hms_mod',
#             'objects': http.request.env['aa_hms_mod.aa_hms_mod'].search([]),
#         })

#     @http.route('/aa_hms_mod/aa_hms_mod/objects/<model("aa_hms_mod.aa_hms_mod"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aa_hms_mod.object', {
#             'object': obj
#         })