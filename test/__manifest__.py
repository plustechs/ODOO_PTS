# -*- coding: utf-8 -*-
{
    'name': "RUC fetch",

    'summary': "Get info from RUC and complete the form",

    'description': "Get info from RUC and complete the form",

    'author': "Plustechs",
    'website': "http://www.plustechs.com",
    'license': 'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'application': True,
    'installable': True,
    'auto_install': False,
    'category': 'Productivity',
    'version': '0.42',

    # any module necessary for this one to work correctly
    # account, contacts, l10n_pe_edi, l10n_pe_edi_stock
    'depends': ['base', 'account', 'contacts', 'l10n_pe_edi', 'l10n_pe_edi_stock', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/test.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
