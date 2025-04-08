from odoo import models, fields, api
from datetime import date


class AccountMove(models.Model):
    _inherit = "account.move"

    pricelist_id = fields.Many2one(
        "product.pricelist",
        string="Tarifa",
        readonly=False,
        states={"posted": [("readonly", True)]},
        help="Lista de precios (Tarifa) aplicada a la factura.",
    )

    @api.onchange("pricelist_id")
    def _onchange_pricelist_id(self):
        """Actualiza los precios de las líneas de la factura cuando cambia la lista de precios."""
        if self.pricelist_id and self.move_type in ("out_invoice", "out_refund"):
            self._update_prices_from_pricelist()

    def _update_prices_from_pricelist(self):
        """Recalcula los precios de las líneas de la factura según la lista de precios."""
        if not self.pricelist_id:
            return

        # Preparar la lista de productos, cantidades y partner para _compute_price_rule
        products_qty_partner = [
            (line.product_id, line.quantity or 1.0, self.partner_id)
            for line in self.invoice_line_ids
            if line.product_id
        ]

        if not products_qty_partner:
            return

        # Calcular los precios usando _compute_price_rule
        prices = self.pricelist_id._compute_price_rule(
            products_qty_partner=products_qty_partner,
            date=date.today(),  # Usamos la fecha actual, puede ajustarse si es necesario
            uom_id=False,  # Dejamos que el método use la UoM del producto por defecto
        )

        # Actualizar los precios de las líneas
        for line in self.invoice_line_ids:
            if line.product_id:
                # Obtener el precio del diccionario retornado por _compute_price_rule
                price, rule_id = prices.get(line.product_id.id, (0.0, False))
                line.price_unit = price

        # Recalcular los totales de la factura
        self._recompute_dynamic_lines(recompute_all_taxes=True)

    @api.model
    def create(self, vals):
        """Sobreescribimos el create para establecer la lista de precios desde el pedido de venta si no está definida."""
        record = super(AccountMove, self).create(vals)
        if not record.pricelist_id and record.invoice_origin:
            sale_order = self.env["sale.order"].search(
                [("name", "=", record.invoice_origin)], limit=1
            )
            if sale_order and sale_order.pricelist_id:
                record.pricelist_id = sale_order.pricelist_id
                record._update_prices_from_pricelist()
        return record
