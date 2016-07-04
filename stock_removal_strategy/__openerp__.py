# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'stock remove strategy',
    'version': '1.1',
    'author': 'binhes',
    'summary': 'Inventory, Logistic, Storage',
    'description': """
Key Features
------------
* stock remove strategy
    """,
    'website': 'http://www.binhes.com',
    'depends': ['stock'],
    'category': 'Warehouse Management',
    'sequence': 16,
    'demo': [
        #'stock_demo_pre.yml',
    ],
    'data': [
        #'pda_commit_workflow.xml',
        #'stock_view.xml',
    ],
    'test': [
        #'test/inventory.yml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'qweb': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
