# -*- coding: utf-8 -*-
{
    'name': "vit_spk",

    'summary': """
        Membuat Report Surat Perintah Kerja""",

    'description': """
        Report Surat perintah Kerja
    """,

    'author': "Iqbal Abdurrahman",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
                'base',
                'stock',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/paperformat.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}