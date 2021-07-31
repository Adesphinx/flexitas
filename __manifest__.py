# -*- coding: utf-8 -*-
{
    'name':        "Gratuity Liability",

    'summary':
                   """
                   This module calculates instantaneous Gratuity Liability for the Organisation 
                   """,

    'description': """
        Manage Gratuity liability for the company, ...
    """,

    'author':      "Adeniyi ITAS",
    'website':     "www.itaslimited.com",

    #
    #
    #
    'category':    'Human Resources',
    'version':     '1.0',

    # any module necessary for this one to work correctly
    'depends':     ['base', 'hr','hr_payroll', 'hr_contract'],

    # always loaded
    'data':        [
        "security/ir.model.access.csv",


    ],
    # only loaded in demonstration mode
    'demo':        [],
    'license': 'AGPL-3',

    'installable': True,
    'application': True,

}
