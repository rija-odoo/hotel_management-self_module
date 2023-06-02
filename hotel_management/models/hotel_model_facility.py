from odoo import fields, models


class HotelModelFacility(models.Model):
    _name = "hotel.model.facility"
    _description = "Hotel Model Facility"

    name = fields.Char()
    color = fields.Integer()
