from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def action_force_cancel(self):
        for picking in self:
            moves = picking.move_ids if "move_ids" in picking._fields else picking.move_lines
            done_moves = moves.filtered(lambda m: m.state == "done")
            done_moves._sm_reverse_done()
            (moves - done_moves).filtered(lambda m: m.state != "cancel")._action_cancel()
        return True


class StockMove(models.Model):
    _inherit = "stock.move"

    def _sm_reverse_done(self):
        Quant = self.env["stock.quant"]
        for move in self:
            for ml in move.move_line_ids:
                qty = ml.quantity if "quantity" in ml._fields else ml.qty_done
                if not qty:
                    continue
                Quant._update_available_quantity(
                    ml.product_id, ml.location_dest_id, -qty,
                    lot_id=ml.lot_id, package_id=ml.result_package_id, owner_id=ml.owner_id,
                )
                Quant._update_available_quantity(
                    ml.product_id, ml.location_id, qty,
                    lot_id=ml.lot_id, package_id=ml.package_id, owner_id=ml.owner_id,
                )
            move.write({"state": "cancel"})
