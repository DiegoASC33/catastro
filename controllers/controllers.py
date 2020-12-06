# -*- coding: utf-8 -*-
from odoo import http

# class Catastro(http.Controller):
#     @http.route('/catastro/catastro/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/catastro/catastro/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('catastro.listing', {
#             'root': '/catastro/catastro',
#             'objects': http.request.env['catastro.catastro'].search([]),
#         })

#     @http.route('/catastro/catastro/objects/<model("catastro.catastro"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('catastro.object', {
#             'object': obj
#         })