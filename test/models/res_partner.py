# -*- coding: utf-8 -*-

from odoo import models, api
import json
import requests


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.depends('vat')
    def _get_ruc(self):
        _headers = {"Content-Type": "application/json",
                    "Accept": "application/json", "Catch-Control": "no-cache"}
        _url_base = "http://54.202.22.62:8080/padron-sunat/ec/gebr/"
        _json_data = {}
        _url_temp = _url_base + self.vat
        response = requests.post(
            _url_temp, data=json.dumps(_json_data), headers=_headers)
        print(json.dumps(response.json(), indent=4, sort_keys=True))
        self.name = response.json()['data'].get('nombreRazonSocial')
        self.street = response.json()['data'].get('nombreVia')


"""     @api.onchange('country_id')
    def _onchange_country(self):
        country = self.country_id or self.company_id.account_fiscal_country_id or self.env.company.account_fiscal_country_id
        identification_type = self.l10n_latam_identification_type_id
        if not identification_type or (identification_type.country_id != country):
            self.l10n_latam_identification_type_id = self.env['l10n_latam.identification.type'].search(
                [('country_id', '=', country.id), ('is_vat', '=', True)], limit=1) or self.env.ref('l10n_latam_base.it_vat', raise_if_not_found=False) """
