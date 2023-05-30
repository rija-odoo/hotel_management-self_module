from odoo import fields, models


class HotelModel(models.Model):
    _name = "hotel.model"
    _description = "Hotel Management"

    name = fields.Char(required=True)
    address = fields.Char()
    city = fields.Char()
    state = fields.Char()
    country = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    website = fields.Char()
    description = fields.Text()
    zip_code=fields.Char()
    star_rating = fields.Selection(
        selection=[
            ('1', '1 Star'),
            ('2', '2 Stars'),
            ('3', '3 Stars'),
            ('4', '4 Stars'),
            ('5', '5 Stars')
        ], string='Star Rating',
    )
    facility = fields.Many2many("hotel.model.facility")
