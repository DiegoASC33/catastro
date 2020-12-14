# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Producto(models.Model):
        _name = 'catastro.producto'
        
        name = fields.Char(String = "Nombre", required=True)
        precio = fields.Integer(String = "Precio", required=True)
        stock = fields.Integer(String = "Stock")

    
