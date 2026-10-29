from odoo import models,fields

class Helado(models.Model):
    #nombre_capeta_base.nombre_clase
    _name = "heladeria.helado"
    _description = "Clase del helado"

    nombreHelado = fields.Char(string="Nombre Helado", required = True, help = "Nombre del helado")
    saborHelado = fields.Char(string="Sabor Helado", required = True, help = "Sabor del helado")
    temperaturaHelado = fields.Integer(string="Temperatura Helado", help ="Temperatura del helado", )
    colorHelado = fields.Char(string="Color Helado", required = True, help = "Color del helado")
    precioHelado = fields.Float(string="Precio Helado", required = True, help = "Precio del helado")
    tamanoHelado = fields.Char(string="Tamaño Helado",required = True, help = "Tamaño del helado")
    
