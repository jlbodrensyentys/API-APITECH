# -*- coding: utf-8 -*-
{
    'name': "Prospect",

    'summary': """
        Adds Is a Prospect in Partner""",

    'description': """
    """,

    'author': "SYENTYS",
    'website': "http://www.syentys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    
    'data': ['views/partner_views.xml'],
}