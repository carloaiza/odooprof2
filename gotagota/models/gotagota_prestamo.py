# -*- coding: utf-8 -*-

from odoo import fields, models


class GotaGotaPrestamo(models.Model):
    _name = 'gotagota.prestamo' # exaflow_documento
    _description = 'Prestamo'
    _order = 'name asc'
    name = fields.Char(string='Descripción', required=True, size=150)
    fecha_prestamo = fields.Date(string='Fecha', required=True)
