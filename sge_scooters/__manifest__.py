# -*- coding: utf-8 -*-
{
    'name': "SGE Scooters Rent and Delivery S.L.",

    'summary': """
        Venta y alquiler de vehículos a particulares""",

    'description': """
        Venta y alquiler de vehículos de locomoción personal y para transporte de cargas
    """,

    'author': "Profesor SGE (copyright by AZF)",
    'website': "https://www.sge_scooters_rent_and_delivery.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/sge_scooters_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/scooters_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
