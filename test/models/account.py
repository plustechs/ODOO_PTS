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
                    response = ruc_fetch(self.ruc)
                    result = request_model_from_dict(json.loads(response))
                    if result.data:
                        _type_of_partner = 'person' if self.ruc[0] == '1' else 'company'
                        _logger.info(result.data)
                        self.partner_id = self.env['res.partner'].create({
                            'name': result.data.nombre_razon_social,
                            'vat': self.ruc,
                            'street_name': result.data.tipo_via+" "+result.data.nombre_via+" "+result.data.numero,
                            'street2': result.data.interior,
                            'country_id': self.env['res.country'].search(
                                [('code', '=', 'PE')]).id,
                            'l10n_latam_identification_type_id': self.env['l10n_latam.identification.type'].search(
                                [('name', '=', 'RUC')]).id,
                            'company_type': _type_of_partner,
                        })
                        _logger.info(self.env['res.country'].search(
                                [('code', '=', 'PE')]).id)
                        _logger.info(self.env['l10n_latam.identification.type'].search(
                                [('name', '=', 'RUC')]).id)
                    else:
                        _logger.info('No se encontró el RUC')
                        self.partner_id = False