from odoo import fields, api, models

class alumnos_model(models.Model):
    _nombre = "instituto_module"
    _description = "Modelo que gestiona la informacion de los alumnos matriculados en los modulos"
    
    nombreAlumno = fields.Char(
        string = "Nombre y Apellidos alumno: "
    )
    
    modulosMatriculado = fields.Many2many(
        string = "Lista de Modulos: ",
        comodel_name = 'insituto_module.modulos_model',
        
        ondelete = 'cascade',
        
    )