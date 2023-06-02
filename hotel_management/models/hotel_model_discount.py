from odoo import fields, models, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError

class HotelModelDiscount(models.Model):
    _name = "hotel.model.discount"
    _description = "Hotel Model discount"

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
            record.room_id.discount_ids.room_status = 'refused'
            record.room_status = 'accepted'
            record.room_id.rent_price = record.price
            record.room_id.state = 'discount_accepted'

    def action_refused(self):
        self.room_status = "refused"
        self.room_id.rent_price = 0

    @api.model
    def create(self, vals):
        temp = self.env['hotel.model'].browse(vals['room_id'])
        temp.state = "discount_received"
        if temp.discount_price >= vals['price']:
            raise UserError(
                "discount price should be greater than existing discount %.2f" % temp.discount_price)
        return super().create(vals)
