from odoo import models, fields

class CreatePersona(models.Model):
    _name="create.persona"
    persona = fields.Char("Nombre")
    apellido = fields.Char("Apellidos")
    direccion = fields.Char("Direccion")
    telefono = fields.Char("Telefono")
    date = fields.Date("Fecha de nacimiento")