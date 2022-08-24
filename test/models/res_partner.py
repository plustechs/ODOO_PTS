# -*- coding: utf-8 -*-

from odoo import models, api
import json
import requests


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.depends('vat', 'l10n_latam_identification_type_id')
    def _get_ruc(self):
        _headers = {"Content-Type": "application/json",
                    "Accept": "application/json", "Catch-Control": "no-cache"}
        _url_base = "http://54.202.22.62:8080/padron-sunat/ec/gebr/20100070970"
        _json_data = {}
        _url_temp = _url_base + self.vat
        response = requests.post(
            _url_temp, data=json.dumps(_json_data), headers=_headers)
        print(json.dumps(response.json(), indent=4, sort_keys=True))

    """@api.constrains('vat', 'l10n_latam_identification_type_id')
    def check_vat(self):
        with_vat = self.filtered(lambda x: x.l10n_latam_identification_type_id.is_vat)
        return super(ResPartner, with_vat).check_vat()"""
