# -*- coding: utf-8 -*-
import datetime
from odoo import fields, models, api, exceptions, _
from odoo.exceptions import ValidationError,UserError
date_format = "%Y-%m-%d"


class MyEmployeeGratuity(models.Model):

    _name = 'my.employee.gratuity'
    _inherit = ['hr.employee', 'hr.contract','mail.thread', 'mail.activity.mixin']
    _description = 'Main Employee Gratuity Calculation'

    name = fields.Char(string= 'Gratuity')
    gratuity_amount = fields.Integer(string="Gratuity Payable", default=0,
                                     readony=True, help=("Gratuity is calculated based on the "
                                    "equation Last salary * Number of years of service  "))


    @api.multi


    def calc_year(self):


        for rec in self:
            employee_id = self.env['hr.employee'].search([])
            worked_years = int(datetime.datetime.now().year) - int(str(self.start_date).split('-')[0])
            self.worked_years = worked_years

            gratuity_amount = wage * worked_years

            return { employee_id: 'employee_id',
                         wage: 'wage',
                        worked_years: 'worked_years'

                     }
