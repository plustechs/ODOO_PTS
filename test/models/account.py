# -*- coding: utf-8 -*-

import json
from odoo import models, fields, api
import logging

from ..models.request import ruc_fetch
from ..models.request_model import RequestModel, request_model_from_dict


_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    ruc = fields.Char(string='RUC')

    @api.onchange('ruc')
    def _search_by_ruc(self):
        _logger.info('=========================')
        if (type(self.ruc) is str):
            _logger.info('str')
            if (self.ruc.isdigit() and len(self.ruc) == 11):
                _logger.info('=========================')
                partner = self.env['res.partner'].search(
                    [('vat', '=', self.ruc)])
                if partner:
                    _logger.info(partner.name)
                    self.partner_id = partner.id
                else:
                    _logger.info('else')
                    response = ruc_fetch(self.ruc)
                    result = request_model_from_dict(json.loads(response))
                    if result.data:
                        _logger.info(result.data)
                        self.partner_id = self.env['res.partner'].create({
                            'name': result.data.nombreRazonSocial,
                            'vat': result.data.ruc,
                            'street_name': result.data.tipoVia+" "+result.data.nombreVia+" "+result.data.numero,
                            'street2': result.data.interior,
                            'country_id': self.env['res.country'].search(
                                [('name', '=', 'Peru')]).id
                        })