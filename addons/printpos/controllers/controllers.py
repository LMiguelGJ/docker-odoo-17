# -*- coding: utf-8 -*-
# from odoo import http


# class Printpos(http.Controller):
#     @http.route('/printpos/printpos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/printpos/printpos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('printpos.listing', {
#             'root': '/printpos/printpos',
#             'objects': http.request.env['printpos.printpos'].search([]),
#         })

#     @http.route('/printpos/printpos/objects/<model("printpos.printpos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('printpos.object', {
#             'object': obj
#         })

