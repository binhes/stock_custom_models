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

from openerp.osv import fields, osv
import logging


_logger = logging.getLogger(__name__)
#----------------------------------------------------------
# Incoterms
#----------------------------------------------------------

class stock_quant(osv.osv):
    _inherit = 'stock.quant'
    _columns = {
        'lot_name': fields.related('lot_id', 'name', type='char', relation='stock_production_lot',string='Lot',store=True, help="lot name"),
    }
    def apply_removal_strategy(self, cr, uid, location, product, quantity, domain, removal_strategy, context=None):
        if removal_strategy == 'fifo':
            order = 'lot_name,in_date, id'
            return self._quants_get_order(cr, uid, location, product, quantity, domain, order, context=context)
        elif removal_strategy == 'lifo':
            order = 'lot_name desc,in_date desc, id desc'
            return self._quants_get_order(cr, uid, location, product, quantity, domain, order, context=context)
        raise osv.except_osv(_('Error!'), _('Removal strategy %s not implemented.' % (removal_strategy,)))
        #return super(stock_quant, self).apply_removal_strategy(cr, uid, location, product, quantity, domain, removal_strategy, context=None)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
