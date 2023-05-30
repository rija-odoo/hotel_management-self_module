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
    zip_code = fields.Char()
    star_rating = fields.Selection(
        selection=[
            ('one', '1 Star'),
            ('two', '2 Stars'),
            ('three', '3 Stars'),
            ('four', '4 Stars'),
            ('five', '5 Stars')
        ], string='Star Rating',
    )
    states=fields.Selection(
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', ' Offer Accepted'), ('booked', 'Booked'), ('canceled', 'Canceled')], copy=True, default='new',
        string='States',
    )
    facility = fields.Many2many("hotel.model.facility")

    room_type_id = fields.Many2one(
        "hotel.model.type", string="room_type")

    offer_ids = fields.One2many(
        "hotel.model.offer", "room_id", string="Offer")

   