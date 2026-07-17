{
    "name": "Force Cancel Sale, Purchase, Picking & Invoice",
    "version": "15.0.1.0.0",
    "category": "Inventory",
    "summary": "Force cancel confirmed/done sale orders, purchase orders, transfers and invoices, reversing stock",
    "description": """
Force Cancel Sale, Purchase, Picking & Invoice
==============================================

Adds Force Cancel buttons to sale orders, purchase orders, stock transfers and
invoices so confirmed or done documents can be cancelled. Cancelling a sale or
purchase order cascades to its transfers and invoices, and done transfers reverse
their stock moves to restore product quantities.
    """,
    "author": "Steven Marp",
    "website": "https://apps.odoo.com/apps/modules/browse?author=Steven Marp",
    "license": "OPL-1",
    "depends": ["sale_management", "purchase", "stock", "account"],
    "data": [
        "views/sale_order_views.xml",
        "views/purchase_order_views.xml",
        "views/stock_picking_views.xml",
        "views/account_move_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": [
        "static/description/banner.gif",
        "static/description/icon.png",
    ],
    "price": 4.99,
    "currency": "USD",
}
