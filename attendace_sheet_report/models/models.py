# -*- coding: utf-8 -*-
import logging
from odoo import models, fields, api
_logger = logging.getLogger(__name__)

class AttendanceInherit(models.Model):

    _inherit = 'hr.attendance'

    work_from = fields.Float(string="Work From",  required=False,compute="_compute_work_from" )
    work_to = fields.Float(string="Work To",  required=False,compute="_compute_work_to" )
    late = fields.Float(string="Late",  required=False, )
    # late = fields.Float(string="Late",  required=False,compute="_compute_late" )


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


    @api.depends('work_from')
    def _compute_late(self):
        from1=0
        work_from_to_time = 0.0
        for rec in self:

            check_in_float = float(str(rec.check_in.hour)+'.'+str(rec.check_in.minute))
            # print(check_in_float)
            # print(rec.work_from  )
            # _logger.info(check_in_float)
            # _logger.info(check_in_float - rec.work_from)
            if check_in_float>rec.work_from:
                # _logger.info("yes")
                # _logger.info(check_in_float-rec.work_from)

                # print(check_in_float-rec.work_from)
                rec.late=check_in_float-rec.work_from
            else:
                rec.late=0
    # def compute_late(self):
    #
    #     check_in_float = float(str(self.check_in.hour) + '.' + str(self.check_in.minute))
    #     # self.late = check_in_float - self.work_from
    #     _logger.info(check_in_float)
    #     _logger.info(type(check_in_float))
    #     _logger.info(type(self.work_from))
    #     _logger.info(self.work_from)
    #     # self.late = check_in_float - self.work_from
    #
    #     if self.work_from<float(check_in_float):
    #         _logger.info(check_in_float-self.work_from)
    #         self.late=check_in_float-self.work_from
    #     else:
    #         _logger.info("noooooooooooooooooooooo")

