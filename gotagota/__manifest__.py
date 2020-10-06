# -*- coding: utf-8 -*-
{
    'name': 'Gota a Gota',
    'version': '12.0.1.0.1',
    'summary': 'Módulo para que mi tío gestione los cobros, y no deba enviar al de la moto',
    'category': 'Cobros',
    'author': 'Carlos Loaiza',
    'maintainer': 'Carlos Loaiza',
    'company': 'Universidad de Manizales',
    'website': 'https://www.umanizales.edu.co',
    'depends': ['mass_mailing'],
    'data': [
        'security/gotagota_security.xml',
        'security/ir.model.access.csv',
        'views/gotagota_prestamo_view.xml',
        'views/gotagota_menu.xml',

        #'views/product_label.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
