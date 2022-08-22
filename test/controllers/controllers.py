# -*- coding: utf-8 -*-
from odoo import http

# this controller is used to fetch data a from a webservice using a parameter and return into accounting module
class AccountingController(http.Controller):
    @http.route('/accounting/<string:param>', type='http', auth='public', website=True)
    def accounting(self, param, **kwargs):
        return http.request.render('accounting.accounting', {'param': param})