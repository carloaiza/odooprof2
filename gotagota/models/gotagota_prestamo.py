# -*- coding: utf-8 -*-

from odoo import fields, models, api
import requests
import json
import logging

_logger = logging.getLogger(__name__)

class GotaGotaPrestamo(models.Model):
    _name = 'gotagota.prestamo'
    _description = 'Prestamo'
    _order = 'name asc'
    name = fields.Char(string='Descripción', required=True, size=150)
    fecha_prestamo = fields.Date(string='Fecha', required=True)
    state = fields.Selection([
        ('enstudio', 'En estudio'),
        ('approved', 'Aprobado'),
        ('refused', 'Rechazado'),
    ], string='Estado', required=True, index=True, track_visibility='onchange', track_sequence=1,
        default='enstudio')
    respuesta = fields.Char(string='Respuesta raspberry', required=True, size=150, default="Sin respuesta")

    @api.multi
    def aprobar_prestamo(self):
        self.write({'state': 'approved'})

    def rechazar_prestamo(self):
        self.write({'state':'refused'})

    def prender_sensor(self):
        _logger.info("json enviado {0} ".format(json.dumps({"nombre":self.name,"fecha":"2020-10-22"})))
        headers = {"Content-Type":"application/json"}
        payload = {"nombre":self.name,"fecha":"2020-10-22"}
        datajson = json.dumps(payload)
        url= "https://requestinspector.com/inspect/01epb0zwgsk4ysvnvahcmhc6ed"
        response = requests.request("POST", url, data=datajson, headers=headers)
        if response.status_code == 200:
            _logger.info("Enviado {}".format(response.content))
            self.write({'respuesta':str(response.content)})



