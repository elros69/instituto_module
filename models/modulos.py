from odoo import  models, fields, api

class modulos(models.Model):
    _name="instituto.modulos"
    _description="Modelo que se encarga de mostrar una lista de modulos impartidos en un grado y su profesor asignado"
    
    nombreModulo = fields.Char(
        string="Modulo: "
    )
    
    gradosPertenece = fields.Many2many(
        string="Grados en los que se Imparte: ",
        comodel_name='instituto.grados',
        
        ondelete = "cascade",
    )
    
    maestrosModulo = fields.Many2one(
        string = "Maestros que Imparten el Modulo: ",
        comodel_name = "instituto.profesores",
        ondelete = "cascade",
    )
    
    alumnosModulo = fields.Many2many(
        string = "Alumnos en el modulo",
        comodel_name = 'instituto.alumnos',
        
        ondelete='cascade',
        
    )