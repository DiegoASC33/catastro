# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Producto(models.Model):
        _name = 'catastro.producto'
        
        name = fields.Char(string = "Nombre", required=True)
        precio = fields.Integer(string = "Precio", required=True)
        stock = fields.Integer( compute = "_actualizar_catastro")

        @api.one
        def _actualizar_catastro(self):
                ventas = self.env['pedido.detalle_boleta'].search([('producto_id', '=', self.id)])
                total_venta = 0
                for venta in ventas:
                        total_venta += ventas.cantidad
                self.stock = 100 + (total_venta)*-1
        
#class MessageBox():
  #      
 #       if self.Stock < 5:
 #               mess = {
#'alerta': _('Baja cantidad de producto'),
  #                      'message' : message
#                }
#def _warning(self):
#if Stock < 15:
#showmessage("Bajo stock")
#else:
# raise Warning(_("Hay productos con bajo stock")