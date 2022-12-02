# -*- coding: utf-8 -*-
# Copyright (c) 2019-Present Droggol. (<https://www.droggol.com/>)

{
    'name': 'WebSite Access',
    'description': 'WebSite Access ',
    'category': 'Theme/eCommerce',
    'version': '16.0.0.0.1',
    'author': 'KHALLOUT Asmaa',
    'depends': ['base','crm'],
    'data': [
        # views
        'views/website_views_inherit.xml',
        'security/ir.model.access.csv',
        'views/menuitems_views.xml',
        'data/website_access_data.xml',
    ],

}
