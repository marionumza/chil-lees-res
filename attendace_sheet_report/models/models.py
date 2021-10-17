# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AttendanceInherit(models.Model):

    _inherit = 'hr.attendance'

    work_from = fields.Float(string="Work From",  required=False,compute="_compute_work_from" )
    work_to = fields.Float(string="Work To",  required=False,compute="_compute_work_to" )


    @api.depends('work_from')
    def _compute_work_from(self):
        from1=0
        for rec in self:
            attend = rec.employee_id.resource_calendar_id.attendance_ids
            for i in attend :
                rec.work_from=i.hour_from

    @api.depends('work_to')
    def _compute_work_to(self):
        to1 = 0
        for rec in self:
            attend = rec.employee_id.resource_calendar_id.attendance_ids
            for i in attend:
                rec.work_to = i.hour_to

