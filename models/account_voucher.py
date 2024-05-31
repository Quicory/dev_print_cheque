# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle 
#
##############################################################################
from odoo import models,fields, api
from odoo import tools

class account_voucher(models.Model):
    _inherit ='account.payment'

    # ref_ncf = fields.Char('Ref. N.C.F')
    
    @api.model
    def _get_check_formate(self):
        company_id = self.env.user.company_id.id
        formate_id = self.env['cheque.setting'].search([('set_default','=',True),('company_id','=',company_id)],limit=1)
        return formate_id.id

    cheque_formate_id = fields.Many2one('cheque.setting', 'Cheque Formate', default=_get_check_formate)
    cheque_no = fields.Char('Cheque No')
    text_free = fields.Char('Concepto')
    partner_text = fields.Char('Partner Title')

    # # @api.depends('partner_bank_id', 'amount', 'ref', 'currency_id', 'journal_id', 'move_id.state',
    # #              'payment_method_line_id', 'payment_type')
    # # def _compute_qr_code(self):
    # #     super()._compute_qr_code(self)
    # @api.onchange('ref')
    # def _onchange_ref(self):
    #     print("QUICO")
    #     # for payment in self:
    #     if self.ref:
    #         refs = self.ref.split(' ')            
    #         print(refs)
    #         ncfs = ""
    #         for ref in refs:
    #             move = self.env['account.move'].search([('name','=',ref)],limit=1)
    #             if move and move.l10n_latam_document_number:
    #                 if ncfs == "":
    #                     ncfs = move.l10n_latam_document_number
    #                 else:
    #                     ncfs += " " + move.l10n_latam_document_number
    #             else:
    #                 if ncfs == "":
    #                     ncfs = ref
    #                 else:
    #                     ncfs += " " + ref

    #         self.ref_ncf = ncfs
    #     else:
    #         self.ref_ncf = ""
    #         #'payment_type': payment.payment_type == 'outbound' and 'inbound' or 'outbound'
    #         # account.internal_type IN ('receivable', 'payable')


    
# vim:expandtab:smartindent:tabstop=4:4softtabstop=4:shiftwidth=4:    
