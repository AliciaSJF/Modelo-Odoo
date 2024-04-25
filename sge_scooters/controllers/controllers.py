# -*- coding: utf-8 -*-
# from odoo import http


# class AzfScooters(http.Controller):
#     @http.route('/azf_scooters/azf_scooters', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/azf_scooters/azf_scooters/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('azf_scooters.listing', {
#             'root': '/azf_scooters/azf_scooters',
#             'objects': http.request.env['azf_scooters.azf_scooters'].search([]),
#         })

#     @http.route('/azf_scooters/azf_scooters/objects/<model("azf_scooters.azf_scooters"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('azf_scooters.object', {
#             'object': obj
#         })
