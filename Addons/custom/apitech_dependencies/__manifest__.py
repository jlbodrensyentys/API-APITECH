# -*- coding: utf-8 -*-
{
    'name': "Apitech - Dependencies",

    'summary': """
        Install modules""",

    'description': """
    """,

    'author': "SYENTYS",
    'website': "http://www.syentys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm', 'account', 'sale_managment', 'stock', 'mrp', 'purchase', 'web_studio', 'mrp_plm'],
    
    'data': [],
}