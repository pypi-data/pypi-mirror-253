# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.tools.translate import _


class cs_task(models.Model):
    _name = 'project.task'
    _inherit = 'project.task'

    related_invoice_id = fields.Many2one(
        'account.invoice', string=_("Invoice"))
