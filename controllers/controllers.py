# -*- coding: utf-8 -*-
# from odoo import http


# class InstitutoModule(http.Controller):
#     @http.route('/instituto_module/instituto_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/instituto_module/instituto_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('instituto_module.listing', {
#             'root': '/instituto_module/instituto_module',
#             'objects': http.request.env['instituto_module.instituto_module'].search([]),
#         })

#     @http.route('/instituto_module/instituto_module/objects/<model("instituto_module.instituto_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('instituto_module.object', {
#             'object': obj
#         })

