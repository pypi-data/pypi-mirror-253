# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _


class smp_teletac(models.Model):
    _inherit = 'smp.sm_teletac'
    _name = 'smp.sm_teletac'

    invoice_report_id = fields.Many2one(
        'sm.invoice_report', string=_("Related invoice report"))
    report_reservation_compute_id = fields.Many2one(
        'smp.sm_report_reservation_compute', string=_("Report"))

    def get_analytic_account(self):
        company = self.env.user.company_id
        analytic_account = company.notfound_teletac_analytic_account_id
        compute = self.reservation_compute_id
        if compute:
            analytic_account = compute.get_teletac_analytic_account()
        return analytic_account


smp_teletac()
