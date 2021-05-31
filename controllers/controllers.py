# -*- coding: utf-8 -*-
from odoo import http

# class MethodCrmEstimatedIncome(http.Controller):
#     @http.route('/method_crm_estimated_income/method_crm_estimated_income/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_crm_estimated_income/method_crm_estimated_income/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_crm_estimated_income.listing', {
#             'root': '/method_crm_estimated_income/method_crm_estimated_income',
#             'objects': http.request.env['method_crm_estimated_income.method_crm_estimated_income'].search([]),
#         })

#     @http.route('/method_crm_estimated_income/method_crm_estimated_income/objects/<model("method_crm_estimated_income.method_crm_estimated_income"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_crm_estimated_income.object', {
#             'object': obj
#         })