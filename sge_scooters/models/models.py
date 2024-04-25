# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class sge_scooters(models.Model):
#     _name = 'sge_scooters.sge_scooters'
#     _description = 'sge_scooters.sge_scooters'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date


class fabricante(models.Model):
    _name = 'sge_scooters.fabricante'
    _description = 'Marca de vehículos alquilados'
    _rec_name = 'marca'

    marca = fields.Char('Marca')
    desc = fields.Text('Description')
    pais = fields.Selection(string='Pais', selection=[('ES','España'),('USA','Estados Unidos'),('CHI','China')], default='ES')
    nvehicles = fields.Integer('Vehículos disponibles', compute='_total_vehicles')
    nbikes = fields.Integer('Nº Bicicletas')
    nscooters = fields.Integer('Nº Scooters')
    ruta = fields.Char('ruta', compute='_pinta_ruta')

    bike_ids = fields.One2many('sge_scooters.ebike', 'fabricante_id', string = 'Modelos de bicicletas')
    scooter_ids = fields.One2many('sge_scooters.scooter', 'fabricante_id', string = 'Modelos de scooters')

    @api.depends('nbikes','nscooters')
    def _total_vehicles(self):
        self.nvehicles = self.nbikes + self.nscooters

    @api.model
    def init(self):
        module_path = self._module
        print("Module Path sge_scooters.fabricante:", module_path)

    def _pinta_ruta(self):
        self.ruta = self._module


class ebike(models.Model):
    _name = 'sge_scooters.ebike'
    _description = 'Bicicletas eléctricas'

    name = fields.Char(string='Modelo')
    peso = fields.Integer('Peso')
    tipo = fields.Selection(string='Tipo', selection=[('ci','Ciudad'),('ca','Carretera'),('pl','Plegable')], default='ci')
    precio = fields.Float('Precio por horas', (5,2))
    motor = fields.Boolean(string='Motor trasero', default=False)
    madein = fields.Selection('Fabricado en', related='fabricante_id.pais', readonly=True)

    clients_id = fields.One2many('sge_scooters.client', 'bike_id', string = 'Reservada por')
    fabricante_id = fields.Many2one('sge_scooters.fabricante', string = 'Fabricante de la bicicleta')


class scooter(models.Model):
    _name = 'sge_scooters.scooter'
    _description = 'Scooter'

    name = fields.Char('Modelo del scooter', required=True) 
    foto = fields.Binary('Fotografia')
    madein = fields.Selection('Fabricado en', related='fabricante_id.pais')
    peso = fields.Integer('Peso del scooter', default = 0)
    precio_hora = fields.Float('Precio por hora', (4, 2), default = 0)
    panel = fields.Boolean('Panel de visualización de velocidad y batería', default=False)
    potencia = fields.Selection(string='Potencia', selection=[('baja','Baja potencia (<250W)'),('media','Media potencia (250-500W)'),('alta','Alta potencia (>500W)')], default='baja')
    fecha_alquiler = fields.Date('Fecha de inicio de alquiler', default = fields.Date.context_today)
    dias_alquiler = fields.Integer('Dias de alquiler', compute='_get_alquiler')

    @api.depends('fecha_alquiler')
    def _get_alquiler(self):
        for scoot in self:
            hoy = date.today()
            scoot.dias_alquiler = relativedelta(hoy, scoot.fecha_alquiler).days

    clients_ids = fields.One2many('sge_scooters.client', 'scooter_id',  string = 'Alquilado por')

    fabricante_id = fields.Many2one('sge_scooters.fabricante', string = 'Fabricante del scooter')


class client(models.Model):
    _name = 'sge_scooters.client'
    _description = 'Clientes de la empresa'

    name = fields.Char('Nombre completo', compute = '_get_full_name')
    codigo = fields.Char('Codigo Cliente', required = True)
    dni = fields.Char('DNI', required = True)
    nombre = fields.Char('Nombre', default='', required = True)
    apellidos = fields.Char('Apellidos', default='', required=True)
    perfil = fields.Image('Foto del perfil', help='Subir fotografía de perfil')

    bike_id = fields.Many2one('sge_scooters.ebike', string = 'Bicicleta alquilada')
    scooter_id = fields.Many2one('sge_scooters.scooter', string = 'Scooter alquilado')

    @api.depends('nombre','apellidos')
    def _get_full_name(self):
        for client in self:
            client.name = client.nombre + ' ' + client.apellidos




