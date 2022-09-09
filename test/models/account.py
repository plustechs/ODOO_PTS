# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging


_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    ruc = fields.Char(string='RUC')

    @api.onchange('ruc')
    def _search_by_ruc(self):
        _logger.info('=========================')
        partner = self.env['res.partner'].search([('vat', '=', self.ruc)])
        _logger.info(partner)
        # if partner:
        #self.partner_id = partner.id
        # _logger.info(self.partner_id)
        # else:
        #self.partner_id = False
        _logger.info(self.partner_id)
