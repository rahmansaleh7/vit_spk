# -*- coding: utf-8 -*-
from odoo import http

# class VitSpk(http.Controller):
#     @http.route('/vit_spk/vit_spk/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_spk/vit_spk/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_spk.listing', {
#             'root': '/vit_spk/vit_spk',
#             'objects': http.request.env['vit_spk.vit_spk'].search([]),
#         })

#     @http.route('/vit_spk/vit_spk/objects/<model("vit_spk.vit_spk"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_spk.object', {
#             'object': obj
#         })