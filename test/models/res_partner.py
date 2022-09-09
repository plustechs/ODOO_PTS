# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json
import requests
import logging


_logger = logging.getLogger(__name__)


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.onchange('vat')
    def _get_ruc(self):
        _logger.info('=========================')
        if (len(str(self.vat)) == 11):
            _logger.info('=========================')
            _logger.info('if')
            _headers = {"Content-Type": "application/json",
                        "Accept": "application/json", "Catch-Control": "no-cache"}
            _url_base = "http://35.90.30.141:8888/padron-sunat/ec/gebr/"
            _json_data = {}
            response = requests.post(
                _url_base+self.vat, data=json.dumps(_json_data), headers=_headers)
            _logger.info(json.dumps(response.json(), indent=4, sort_keys=True))
            respose_data = response.json().get('data')
            self.name = respose_data.get('nombreRazonSocial')
            self.street = respose_data.get(
                "nombreVia")+respose_data.get("numero")+respose_data.get("tipoVia")


"""     @api.onchange('country_id')
    def _onchange_country(self):
        country = self.country_id or self.company_id.account_fiscal_country_id or self.env.company.account_fiscal_country_id
        identification_type = self.l10n_latam_identification_type_id
        if not identification_type or (identification_type.country_id != country):
            self.l10n_latam_identification_type_id = self.env['l10n_latam.identification.type'].search(
                [('country_id', '=', country.id), ('is_vat', '=', True)], limit=1) or self.env.ref('l10n_latam_base.it_vat', raise_if_not_found=False) """
