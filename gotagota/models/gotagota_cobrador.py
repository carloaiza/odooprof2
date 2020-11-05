# -*- coding: utf-8 -*-

from odoo import fields, models


class GotaGotaCobrador(models.Model):
    _name = 'gotagota.cobrador' # exaflow_documento
    _description = 'Cobrador'
    _order = 'name asc'
    name = fields.Char(string='Nombre', required=True, size=150,index=True)
    documento = fields.Char(string='Número de documento', required=True, size=20,index=True)
    tipodocumento = fields.Selection(
        [('1', 'Cédula de ciudadanía'),
         ('2', 'NIT'),
         ('3', 'Cedula de extranjeria'),
         ('4', 'Pasaporte'),
         ], string='Tipo de Documento', required=True, index=True, track_visibility='onchange',
        track_sequence=3, default="1")
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)
    ciudades_ids = fields.One2many('gotagota.cobrador.ciudad', 'cobrador_id', 'Ciudades',
                                      track_visibility='onchange')
    _sql_constraints = {('cobrador_uniq', 'unique(documento)', 'El número de documento debe ser único')}

class GotaGotaDepartamento(models.Model):
    _name = 'gotagota.departamento'  # exaflow_documento
    _description = 'Departamento'
    _order = 'name asc'
    name = fields.Char(string='Nombre', required=True, size=50, index=True)
    codigo = fields.Char(string='Código', required=True, size=20, index=True)
    _sql_constraints = {('departamento_uniq', 'unique(codigo)', 'El código del departamento debe ser único')}

class GotaGotaCiudad(models.Model):
    _name = 'gotagota.ciudad'  # exaflow_documento
    _description = 'Ciudad'
    _order = 'name asc'
    name = fields.Char(string='Nombre', required=True, size=50, index=True)
    codigo = fields.Char(string='Código', required=True, size=20, index=True)
    #Relación
    departamento_id = fields.Many2one('gotagota.departamento', 'Departamento', required=True)
    cobradores_ids = fields.One2many('gotagota.cobrador.ciudad', 'ciudad_id', 'Cobradores',
                                   track_visibility='onchange')
    _sql_constraints = {('ciudad_uniq', 'unique(codigo)', 'El código de la ciudad debe ser único')}


class GotaGotaCobradorCiudad(models.Model):
    _name = 'gotagota.cobrador.ciudad'
    _description = 'Relación Cobrador Ciudad'
    cobrador_id = fields.Many2one('gotagota.cobrador', 'Cobrador', required=True, index=True)
    ciudad_id = fields.Many2one('gotagota.ciudad', 'Ciudad', required=True, index=True)
    _sql_constraints = [('cobrador_ciudad_uniq', 'unique(cobrador_id, ciudad_id)',
                         'Ya existe la asociación ingresada del cobrador y la ciudad')]






