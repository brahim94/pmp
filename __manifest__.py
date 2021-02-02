# -*- coding: utf-8 -*-
{
    'name': "pmp_report",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'web', 'point_of_sale', 'delivery'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/layouts.xml',
        'data/sequence.xml',
        'views/pmp_stock_picking_view.xml',
        # 'static/src/attempt_inherit_pos_qweb.xml',        
        'report/pmp_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
