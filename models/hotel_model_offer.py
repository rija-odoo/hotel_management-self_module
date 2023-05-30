from odoo import fields, models


class HotelModelOffer(models.Model):
    _name = "hotel.model.offer"
    _description = "Hotel Model Offer"

    price = fields.Float()
    customer_id = fields.Many2one(
        "res.partner", required=True, string="Customer")
    room_type = fields.Integer(string="Room Type")
    room_status= fields.Selection(
        selection=[("room_booked", "Room_Booked")], copy=False
    )
