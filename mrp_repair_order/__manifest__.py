# -*- coding: utf-8 -*-
{
    'name': "MRP repair order",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Yziact",
    'maintainer': 'Aurelien ROY',

    # lien vers le dépôt git ou site Yziact
    'website': "http://gitlab.yziact.net/odoo/petit/addons",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'base_automation',
        'stock',
        'sale',
        'partner_references',
        'mrp',
        'mrp_workorder',
        'quality',
        'quality_mrp',
        'mrp_repair_model',
        'material_request',
        'custom_popup',
    ],
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/ir_sequence_data.xml',
        'data/ir.actions.server.csv',
        'data/base.automation.csv',
        'data/stock.picking.type.csv',
        'views/mrp_repair_order.xml',
        'views/mrp_workorder.xml',
        'views/mrp_routing_workcenter.xml',
        'views/mrp_production.xml',
        'views/quality_point.xml',
        'views/sale_order.xml',
        'views/res_partner.xml',
        'views/account_invoice.xml',
        'views/stock_move.xml',
        'views/mrp_workcenter_productivity.xml',
        'views/res_config_settings_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False, 

    # Hooks for module installation/uninstallation, their value should be a string
    # representing the name of a function defined inside the module's __init__.py.
    # 'pre_init_hook': '',
    # 'post_init_hook': '',
    # 'uninstall_hook': '',
}