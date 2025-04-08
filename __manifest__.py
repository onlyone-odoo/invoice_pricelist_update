{
    "name": "Invoice Pricelist Update",
    "version": "15.0.2.0.0",
    "depends": ["account", "sale"],
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "license": "AGPL-3",
    "category": "Accounting",
    "description": """
        Module to update invoice amounts based on selected pricelist (Tarifa).
        Allows changing the pricelist on the invoice and automatically recalculates the amounts.
    """,
    "data": [
        "views/account_move_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
