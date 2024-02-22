from odoo import models, fields, api

class grados(models.Model):
    _name="instituto.grados"
    _description="Modulo de odoo que se encarga de mostrar una lista de grados y sus modulos"
    
    nombreGrado = fields.Char(
        string="Grado: "
    )
    
    listaModulos = fields.Many2many(
        string="Lista de Modulos que se Imparten: ",
        comodel_name='instituto.modulos',
        ondelete="cascade",
    )