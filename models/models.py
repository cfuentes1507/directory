# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DirectorioRol(models.Model):
    _name = 'directorio.rol'
    _description = 'Rol o Etiqueta para Contactos del Directorio'

    name = fields.Char(string="Nombre del Rol", required=True)
    
class DirectorioTelefono(models.Model):
    _name = 'directorio.telefono'
    _description = 'Número de Teléfono para Contacto del Directorio'

    numero = fields.Char(string="Número de Teléfono", required=True)
    contacto_id = fields.Many2one('directorio.contacto', string="Contacto", ondelete='cascade')

class DirectorioContacto(models.Model):
    _name = 'directorio.contacto'
    _description = 'Contacto del Directorio Telefónico'
    _order = 'name'

    # Campos para Individuo
    nombre = fields.Char(string="Nombre", required=True)
    apellido = fields.Char(string="Apellido", required=True)
    # El nombre completo se calcula a partir de nombre y apellido
    name = fields.Char(string="Nombre Completo", compute='_compute_name', inverse='_inverse_name', store=True)

    image_1920 = fields.Image(string="Imagen")
    email = fields.Char(string="Email")
    function = fields.Char(string="Cargo / Puesto")
    notes = fields.Text(string="Notas")

    # Campos de Dirección
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char()
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='Estado/Provincia')
    country_id = fields.Many2one('res.country', string='País')

    telefono_ids = fields.One2many('directorio.telefono', 'contacto_id', string="Teléfonos")
    rol_ids = fields.Many2many('directorio.rol', string="Roles/Etiquetas")

    @api.depends('nombre', 'apellido')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.nombre or ''} {record.apellido or ''}".strip()

    def _inverse_name(self):
        for record in self:
            # Permite editar el nombre completo y que se actualicen nombre y apellido
            parts = record.name.split(' ', 1)
            record.nombre = parts[0]
            record.apellido = parts[1] if len(parts) > 1 else ''
