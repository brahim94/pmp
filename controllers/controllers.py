# -*- coding: utf-8 -*-
# from odoo import http


# class PmpReport(http.Controller):
#     @http.route('/pmp_report/pmp_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pmp_report/pmp_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pmp_report.listing', {
#             'root': '/pmp_report/pmp_report',
#             'objects': http.request.env['pmp_report.pmp_report'].search([]),
#         })

#     @http.route('/pmp_report/pmp_report/objects/<model("pmp_report.pmp_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pmp_report.object', {
#             'object': obj
#         })
