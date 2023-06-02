from odoo import models, Command


class HotelModel(models.Model):
    _inherit = "hotel.model"

    def action_booked(self):
        self.env['account.move'].create({
            'partner_id': self.id,
            'move_type': 'out_invoice',
            "line_ids": [
                Command.create({
                    'name': self.name,
                    'quantity': 1,
                    'price_unit': self.discount_price
                }),
                Command.create({
                    'name': 'GST fees',
                    'quantity': 1,
                    'price_unit': 65
                })
            ]
        })
        return super(HotelModel, self).action_booked()
