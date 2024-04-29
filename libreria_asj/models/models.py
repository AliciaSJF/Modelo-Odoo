# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class libreria_asj(models.Model):
#     _name = 'libreria_asj.libreria_asj'
#     _description = 'libreria_asj.libreria_asj'

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

class libro(models.Model):

    _name = 'libreria_asj.libro'
    _description = 'libreria_asj.libro'

    name = fields.Char(string='Titulo', required=True)
    isbn = fields.Integer(string='ISBN', required=True)
    portada = fields.Binary('Fotografia')
    precio = fields.Float(string='Precio')
    descripcion = fields.Text()
    anio_salida = fields.Date()
    genero = fields.Selection(string='Genero', selection=[('pol','Policiaca'),('fic','Ficcion'),('nov','Novela'),('inf','Infantil')], default='fic')
    edicion = fields.Integer()
    autor_id = fields.Many2one('libreria_asj.autor', string = 'Autor')
    editoriales_ids = fields.Many2many('libreria_asj.editorial', string = 'Editorial')
    cliente_ids = fields.Many2one('libreria_asj.cliente', string = 'Cliente')


class autor(models.Model):
    _name = 'libreria_asj.autor'
    _description = 'libreria_asj.autor'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    nacionalidad = fields.Char(string='Nacionalidad', required=True)
    libros_ids = fields.One2many('libreria_asj.libro', 'autor_id', string='Libros')
#    clientes_ids = fields.Many2many('libreria_asj.cliente', string='Clientes')
    # Campo calculado para contar los libros del autor
    total_libros = fields.Integer(string='Total de Libros', compute='_calcular_total_libros', store=True, readonly=True)

    @api.depends('libros_ids')
    def _calcular_total_libros(self):
        for autor in self:
            autor.total_libros = len(autor.libros_ids)
    

class editorial(models.Model):
    _name = 'libreria_asj.editorial'
    _description = 'libreria_asj.editorial'

    name = fields.Char(string='Nombre', required=True)
    telefono = fields.Char(string='Telefono', required=True)
    email = fields.Char(string='Email', required=True)
    direccion = fields.Char(string='Direccion', required=True)
    pais = fields.Selection(string='Pais', selection=[('ES','España'),('FR','Francia'),('IT','Italia')], default='ES')
    codigo_postal = fields.Integer()
    libros_ids = fields.Many2many('libreria_asj.libro', string='Libros')   

class cliente (models.Model):
    _name = 'libreria_asj.cliente'
    _description = 'libreria_asj.cliente'

    name = fields.Char(string='Nombre', required=True)
    apellidos = fields.Char(string='Apellidos', required=True)
    dni = fields.Char(string='DNI', required=True)
    libros_ids = fields.One2many('libreria_asj.libro', 'cliente_ids',  string='Libros')

class prestamo (models.Model):
    _name = 'libreria_asj.prestamo'
    _description = 'libreria_asj.prestamo'

    codigo = fields.Char(string='Codigo', required=True)
    fecha_prestamo = fields.Date()
    fecha_devolucion = fields.Date()
    cliente_id = fields.Many2one('libreria_asj.cliente', string = 'Cliente')
    libro_id = fields.Many2one('libreria_asj.libro', string = 'Libro')