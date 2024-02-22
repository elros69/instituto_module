# -*- coding: utf-8 -*-
{
    'name': "instituto",

    'summary': "Modulo creado para la gestion de los cursos, profesor y alumnos de un instituto",

    'description': """
Este modulo permite gestionar, almacenar y visualizar diferentes
aspectos informativos y de gestion de un instituto.
Pudiendo visualizar los modulos impartidos en este,
la plantilla de profesores y su informacion relacionada a ellos
mas aparte los alumnos integros de la institucion.
    """,

    'author': "Abraham Campoy Garica",
    'website': "https://github.com/elros69",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Administracion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/gradosView.xml',
        'views/modulosView.xml',
        'views/profesoresView.xml',
        'views/alumnosView.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

