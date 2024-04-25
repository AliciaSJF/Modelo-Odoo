# -*- coding: utf-8 -*-
# from odoo import http


# class LibreriaAsj(http.Controller):
#     @http.route('/libreria_asj/libreria_asj', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libreria_asj/libreria_asj/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('libreria_asj.listing', {
#             'root': '/libreria_asj/libreria_asj',
#             'objects': http.request.env['libreria_asj.libreria_asj'].search([]),
#         })

#     @http.route('/libreria_asj/libreria_asj/objects/<model("libreria_asj.libreria_asj"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libreria_asj.object', {
#             'object': obj
#         })
