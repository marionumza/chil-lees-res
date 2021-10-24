# -*- coding: utf-8 -*-

from odoo import models, fields, api


class add_currency(models.Model):
    _inherit = 'hr.contract'

    curr = fields.Selection(string="العمله", selection=[('dollar', 'الدولار'), ('dinar', 'الدينار العراقي'), ], required=False, )
    wage = fields.Float('Wage', required=True, tracking=True, help="Employee's monthly gross wage.")


class HREmployee(models.Model):
    _inherit = 'hr.employee'

    pre_job = fields.Char(string="Previous Job ", required=False, )
