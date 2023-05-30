from odoo import fields, models


class HotelModelOffer(models.Model):
    _name = "hotel.model.offer"
    _description = "Hotel Model Offer"

    price = fields.Float()

    room_status = fields.Selection(
        selection=[("accepted", "Accepted"), ("refused", "Refused")], copy=False
    )
    room_id = fields.Many2one(
        "hotel.model", required=True, string="Room")

    customer_id = fields.Many2one(
        "res.partner", required=True, string="Customer")

    def action_accepted(self):
        for record in self:
            record.room_id.offer_ids.room_status = 'refused'
            record.room_status = 'accepted'
            record.room_id.states = 'offer_accepted'

    def action_refused(self):
        self.room_status = "refused"
