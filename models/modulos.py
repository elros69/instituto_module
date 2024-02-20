from odoo import  models, fields, api

class modulos_model(models.Model):
    _name = "instituto_module.modulos_model"
    _description = "Modelo que se encarga de mostrar una lista de modulos impartidos en un grado y su profesor asignado"
    
    nombreModulo = fields.Char(
        string = "Modulo: "
    )
    
    gradosPertenece = fields.Many2many(
        string = "Grados en los que se Imparte: ",
        comodel_name = 'instituto_module.grados_model',
        
        ondelete = "cascade",
    )
    
    maestrosModulo = fields.Many2one(
        string = "Maestros que Imparten el Modulo: ",
        comodel_name = "instituto_module.profesores_model",
        ondelete = "cascade",
    )
    
    alumnosModulo = fields.Many2many(
        string = "Alumnos en el modulo",
        comodel_name = 'instituto_module.alumnos_model',
        
        ondelete='cascade',
        
    )