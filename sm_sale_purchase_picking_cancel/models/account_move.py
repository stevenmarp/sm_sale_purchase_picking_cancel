from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def action_force_cancel(self):
        for move in self:
            if move.state == "cancel":
                continue
            if move.state == "posted":
                move.button_draft()
            move.button_cancel()
        return True
