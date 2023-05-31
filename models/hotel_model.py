from odoo import api, fields, models, exceptions
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero


class HotelModel(models.Model):
    _name = "hotel.model"
    _description = "Hotel Management"

    name = fields.Char(required=True)
    city = fields.Char()
    states = fields.Char()
    country = fields.Char()
    rent_price = fields.Float(readonly=True, copy=False)
    offer_price = fields.Float(
        string="Offer Price", compute="_compute_offer_price")
    expected_price = fields.Float()
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
    state = fields.Selection(
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', ' Offer Accepted'), ('booked', 'Booked'), ('canceled', 'Canceled')], copy=True, default='new',
        string='State',
    )
    facility = fields.Many2many("hotel.model.facility")

    image=fields.Binary()

    room_type_id = fields.Many2one(
        "hotel.model.type", string="room_type")

    offer_ids = fields.One2many(
        "hotel.model.offer", "room_id", string="Offer")

    def action_booked(self):
        if self.state == "canceled":
            raise UserError("Cancled Room can't be booked")
        else:
            self.state = "booked"
        return True

    def action_cancled(self):
        if self.state == "booked":
            raise UserError("booked Room can't be cancled")
        else:
            self.state = "canceled"
        return True

    @api.constrains("expected_price", "rent_price")
    def _check_rent_price(self):
        for record in self:
            if (
                not float_is_zero(record.rent_price, precision_digits=2)
                and not float_is_zero(record.expected_price, precision_digits=2)
                and float_compare(record.rent_price, 0.9 * record.expected_price, precision_digits=2) == -1
            ):
                raise ValidationError(
                    "rent price cannot be lower than 90% of the expected price.")



    @api.depends("offer_ids.price")
    def _compute_offer_price(self):
        for record in self:
            if (record.mapped('offer_ids.price')):
                record.offer_price = max(record.mapped('offer_ids.price'))
            else:
                record.offer_price = 0
