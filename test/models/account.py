# -*- coding: utf-8 -*-

import json
from odoo import models, fields, api
import logging

from test.models.request import ruc_fetch
from test.models.request_model import request_model_from_dict


_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    ruc = fields.Char(string='RUC')

    @api.onchange('ruc')
    def _search_by_ruc(self):
        if(len(str(self.ruc)) == 11):
            _logger.info('=========================')
            partner = self.env['res.partner'].search([('vat', '=', self.ruc)])
            if partner:
                _logger.info(partner.name)
                self.partner_id = partner.id
            else:
                _logger.info('else')
                response = ruc_fetch(self.ruc)
                result = request_model_from_dict(json.loads(response))
                _logger.info(result.data)
                #self.partner_id = self.env['res.partner'].create(
                #    {'name': 'Nuevo', 'vat': self.ruc}).id
