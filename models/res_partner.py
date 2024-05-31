# -*- coding: utf-8 -*-
##############################################################################
#
#    BILL Software
#    Copyright (C) 2023 (<http://billsoftware.com.do>).
#
#    For Module Support : 
#
##############################################################################
from odoo import api, fields, models

class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
     
    commercial_name = fields.Char('Nombre Comercial')
