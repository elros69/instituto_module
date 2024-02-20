from odoo import models, fields, api

class profesores_model(models.Model):
    _name = "instituto_module.profesores_model"
    _description = "Modelo que se encarga de administrar la informacion de los maestros"
    
    nombreMaestro = fields.Char(
        String = "Nombre y Apellido Profesor: ",
    )
    dni = fields.Char(
        string = "DNI: "
    )
    modulosImpartidos = fields.One2many(
        string = "Modulos que imparte: ",
        comodel_name = "instituto_module.modulos_model",
        inverse_name = "maestrosModulo",
    )