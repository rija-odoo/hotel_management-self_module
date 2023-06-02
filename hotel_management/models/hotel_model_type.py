from odoo import fields, models, api


class HotelModelType(models.Model):
    _name = "hotel.model.type"
    _description = "Hotel Model Type"

    name = fields.Char(required=True)
    room_rent=fields.Integer()

