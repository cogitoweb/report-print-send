# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

import logging
_logger = logging.getLogger(__name__)


class IrActionsReportAutoPrint(models.Model):

    _name = 'ir.actions.report.auto.print'
    _description = "Autoprint settings"

    # Fields declaration

    report_id = fields.Many2one(
        string="Report",
        comodel_name='ir.actions.report.xml',
        required=True
    )

    printer_id = fields.Many2one(
        string="Printer",
        comodel_name='printing.printer',
        required=True
    )

    copies = fields.Integer(
        string="Copies",
        required=True
    )
