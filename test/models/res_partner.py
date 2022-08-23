# -*- coding: utf-8 -*-

from odoo import models, fields, api
import json
import requests

headers = {"Content-Type": "application/json",
           "Accept": "application/json", "Catch-Control": "no-cache"}
url_base = "http://54.202.22.62:8080/padron-sunat/ec/gebr/20100070970"
json_data = {}


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.depends('vat', 'l10n_latam_identification_type_id')
    def _get_ruc(self):
        response = requests.post(
            url_base, data=json.dumps(json_data), headers=headers)
        print(json.dumps(response.json(), indent=4, sort_keys=True))

    """@api.constrains('vat', 'l10n_latam_identification_type_id')
    def check_vat(self):
        with_vat = self.filtered(lambda x: x.l10n_latam_identification_type_id.is_vat)
        return super(ResPartner, with_vat).check_vat()"""
