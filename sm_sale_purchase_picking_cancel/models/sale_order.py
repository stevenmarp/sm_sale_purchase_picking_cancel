from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_force_cancel(self):
        for order in self:
            order.invoice_ids.filtered(lambda m: m.state != "cancel").action_force_cancel()
            order.picking_ids.filtered(lambda p: p.state != "cancel").action_force_cancel()
            order.write({"state": "cancel"})
        return True
