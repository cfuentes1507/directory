# -*- coding: utf-8 -*-
{
    'name': 'Directorio Telefónico (Independiente)',
    'version': '15.0.1.0.0',
    'summary': 'Aplicación de directorio telefónico autocontenida.',
    'author': 'My Company',
    'website': 'http://www.yourcompany.com',
    'category': 'Tools',
    'depends': ['base'], # ¡Solo depende de base, no de contacts!
    'data': [
        'security/directory_security.xml',
        'security/ir.model.access.csv',
        'data/directorio_rol_data.xml',
        'views/directorio_views.xml',
        'views/directorio_menus.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True, # Lo marcamos como una aplicación principal
    'installable': True,
}
