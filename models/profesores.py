from odoo import models, fields, api

class profesores(models.Model):
    _name="instituto.profesores"
    _description="Modelo que se encarga de administrar la informacion de los maestros"
    
    nombreMaestro = fields.Char(
        String="Nombre y Apellido Profesor: ",
    )
    dni = fields.Char(
        string="DNI: "
    )
    modulosImpartidos = fields.One2many(
        string="Modulos que imparte: ",
        comodel_name="instituto.modulos",
        inverse_name="maestrosModulo",
    )