from odoo import fields, api, models

class alumnos(models.Model):
    _name="instituto.alumnos"
    _description="Modelo que gestiona la informacion de los alumnos matriculados en los modulos"
    
    nombreAlumno=fields.Char(
        string="Nombre y Apellidos alumno: "
    )
    
    modulosMatriculado = fields.Many2many(
        string = "Lista de Modulos: ",
        comodel_name = 'insituto.modulos',
        
        ondelete = 'cascade',
        
    )