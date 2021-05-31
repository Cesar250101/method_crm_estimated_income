# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Crm(models.Model):
    _inherit = 'crm.lead'
    
    planned_revenue = fields.Monetary('Expected Revenue', compute='_compute_sale_order_amount_total',currency_field='company_currency', track_visibility='always')

    
    @api.onchange('order_ids')
    def _compute_sale_order_amount_total(self):
        for lead in self:
            total = 0.0
            nbr = 0
            company_currency = lead.company_currency or self.env.user.company_id.currency_id
            for order in lead.order_ids:
                if order.state in ('draft','sent'):
                    total += order.currency_id._convert(
                        order.amount_untaxed, company_currency, order.company_id, order.date_order or fields.Date.today())
            if total>0:
                lead.planned_revenue = total