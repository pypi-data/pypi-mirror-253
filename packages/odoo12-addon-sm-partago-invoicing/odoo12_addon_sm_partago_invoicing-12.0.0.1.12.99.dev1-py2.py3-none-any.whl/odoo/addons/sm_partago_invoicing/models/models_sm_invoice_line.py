# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.tools.translate import _


class smp_invoice_line(models.Model):
    _inherit = 'account.invoice.line'
    _name = 'account.invoice.line'

    related_tariff_id = fields.Many2one(
        'smp.sm_carsharing_tariff',
        string=_("Related tariff")
    )
    related_reservation_compute_id = fields.Many2one(
        'smp.sm_reservation_compute',
        string=_("Related reservation compute")
    )
    invoice_report_id = fields.Many2one(
        'sm.invoice_report',
        string=_("Related invoice report")
    )
    partner_id = fields.Many2one(
        'res.partner',
        string=_("Related partner (inv_report)")
    )
    initial_price_computed = fields.Float(
        string=_("Initial price"),
        compute="_get_line_initial_price",
        store=False
    )
    line_type = fields.Selection([
        ('default', 'Default'),
        ('cs_default', 'Carsharing default'),
        ('cs_extra', 'Carsharing extra time'),
        ('cs_teletac', 'Teletac'),
        ('cs_discount', 'Discount'),
        ('cs_penalty', 'Penalty')],
        string=_("Line type"),
        default="default"
    )
    penalty_type = fields.Selection([
        ('none', 'None'),
        ('general', 'General'),
        ('unused', 'Unused'),
        ('cancelled', 'Cancelled')],
        string=_("Penalty type"),
        default="none"
    )
    parent_invoice_line_id = fields.Many2one(
        'account.invoice.line',
        string=_("Parent invoice line (penalties)")
    )
    related_reservation_cancelled = fields.Boolean(
        string=_("Related reservation cancelled"),
        compute="_get_related_reservation_cancelled"
    )

    @api.depends('related_reservation_compute_id')
    def _get_related_reservation_cancelled(self):
        for record in self:
            record.related_reservation_cancelled = False
            if record.related_reservation_compute_id:
                record.related_reservation_cancelled = \
                    record.related_reservation_compute_id.compute_cancelled

    @api.depends('related_reservation_compute_id')
    def _get_line_initial_price(self):
        for record in self:
            record.initial_price_computed = 0
            if record.related_reservation_compute_id.id is not False:
                if (
                    record.related_reservation_compute_id.carconfig_id.id is not
                    False
                ):
                    record.initial_price_computed = record.related_reservation_compute_id.cs_carconfig_id.initial_price


smp_invoice_line()
