===========
Invoice Pricelist Update
===========

.. |badge1| image:: https://img.shields.io/badge/maturity-Stable-brightgreen
    :target: https://odoo-community.org/page/development-status
    :alt: Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

.. |badge3| image:: https://onlyone.odoo.com/web/image/website/1/logo/OnlyOne%20Soft?unique=dccda5b
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge1| |badge2| |badge3|

This module extends the functionality of the Accounting module to support dynamic updates of invoice amounts based on the selected pricelist (referred to as "Tarifa"). It allows you to change the pricelist directly on an invoice and automatically recalculates the line prices and totals accordingly, even if the pricelist differs from the one used in the related sales order.

**Table of contents**

.. contents::
   :local:

Install
=======

To install this module, you need to:

1. Place the `invoice_pricelist_update` folder in your Odoo addons directory.
2. Go to *Apps* in your Odoo instance, search for "Invoice Pricelist Update", and click *Install*.
3. Ensure that the `account` and `sale` modules are already installed, as they are dependencies of this module.

Usage
=====

1. Go to *Accounting > Customers > Invoices* or *Invoicing > Customers > Invoices* (depending on your Odoo configuration).
2. Create or edit an invoice. If the invoice is created from a sales order, the pricelist will be automatically inherited from the sales order.
3. In the invoice form, you will see the "Tarifa" field (pricelist) located just below the "Customer" field. Select a different pricelist if needed.
4. Upon changing the pricelist, the module will automatically update the unit prices of the invoice lines based on the selected pricelist and recalculate the taxes and totals.

Known issues / Roadmap
======================

* **Known Issues**: None identified at this time.
* **Roadmap**:
  - Add support for handling specific tax scenarios where the pricelist change might affect tax calculations differently.
  - Include an option to log pricelist changes in the invoice chatter for better traceability.

Bug Tracker
===========

For any issues or questions, please contact our support team at:

* Help Contact: `support@onlyone.odoo.com <mailto:support@onlyone.odoo.com>`_

Credits
=======

Authors
~~~~~~~

* Be OnlyOne

Contributors
~~~~~~~~~~~~

* `Be OnlyOne. <https://onlyone.odoo.com/>`_
  
  * Matías Bressanello

Maintainers
~~~~~~~~~~~

This module is maintained by Be OnlyOne