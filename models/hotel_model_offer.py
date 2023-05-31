from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

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
            record.room_id.rent_price = record.price
            record.room_id.state = 'offer_accepted'

    def action_refused(self):
        self.room_status = "refused"
        self.room_id.rent_price = 0

    @api.model
    def create(self, vals):
        temp = self.env['hotel.model'].browse(vals['room_id'])
        temp.state = "offer_received"
        if temp.offer_price >= vals['price']:
            raise UserError(
                "offer price should be greater than existing offer %.2f" % temp.offer_price)
        return super().create(vals)
