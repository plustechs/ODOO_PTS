# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json
import requests
import logging


_logger = logging.getLogger(__name__)
_logger.info('Start')


class ResPartner(models.Model):
    # inherit the model res.partner from l10n_latam_base
    _inherit = 'res.partner'

    rucName = fields.Char(string='Ruc Name', related='vat')

    @api.onchange('vat')
    def _get_ruc(self):
        _headers = {"Content-Type": "application/json",
                    "Accept": "application/json", "Catch-Control": "no-cache"}
        _url_base = "http://35.90.30.141:8888/padron-sunat/ec/gebr/"
        _json_data = {}
        _url_temp = _url_base + self.rucName
        response = requests.post(
            _url_temp, data=json.dumps(_json_data), headers=_headers)
        _logger.info(json.dumps(response.json(), indent=4, sort_keys=True))
        # update self.name with response.data.name
        _logger.info(self.name)
        if response.json()['data'] is not None:
            self.name = response.json()['data']['nombreRazonSocial']
            self.street_name = response.json()['data']['nombreVia'] + ' ' + response.json()['data']['numeroVia']
            #self.env.cr.commit()
        #write the response in the log
        _logger.info(self.name)


"""     @api.onchange('country_id')
    def _onchange_country(self):
        country = self.country_id or self.company_id.account_fiscal_country_id or self.env.company.account_fiscal_country_id
        identification_type = self.l10n_latam_identification_type_id
        if not identification_type or (identification_type.country_id != country):
            self.l10n_latam_identification_type_id = self.env['l10n_latam.identification.type'].search(
                [('country_id', '=', country.id), ('is_vat', '=', True)], limit=1) or self.env.ref('l10n_latam_base.it_vat', raise_if_not_found=False) """
