# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TestModel(models.Model):
    _name = 'test.model'
    _description = 'Test Model'

    name = fields.Char(string='Name', required=True)
    value = fields.Integer(string='Value', required=True)
    age = fields.Integer(string='Age', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                              ('other', 'Other')], required=True, default='other')
    description = fields.Text(string='Description')