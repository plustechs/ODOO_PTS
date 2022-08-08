# -*- coding: utf-8 -*-
{
    'name': "test",

    'summary': """
        Test module for Odoo
        """,

    'description': """
        Test module for Odoo
    """,

    'author': "Plustechs",
    'website': "http://www.plustechs.com",
    'license': 'LGPL-3',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'application': True,
    'installable': True,
    'category': 'Productivity',
    'version': '0.42',

    # any module necessary for this one to work correctly
    'depends': ['base'],

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
