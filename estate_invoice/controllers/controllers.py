# -*- coding: utf-8 -*-
# from odoo import http


# class EstateInvoice(http.Controller):
#     @http.route('/estate_invoice/estate_invoice', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estate_invoice/estate_invoice/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('estate_invoice.listing', {
#             'root': '/estate_invoice/estate_invoice',
#             'objects': http.request.env['estate_invoice.estate_invoice'].search([]),
#         })

#     @http.route('/estate_invoice/estate_invoice/objects/<model("estate_invoice.estate_invoice"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estate_invoice.object', {
#             'object': obj
#         })
