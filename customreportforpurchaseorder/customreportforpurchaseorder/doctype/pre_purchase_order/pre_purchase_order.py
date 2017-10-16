# -*- coding: utf-8 -*-
# Copyright (c) 2017, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PrePurchaseOrder(Document):
	def on_submit(self):
                last_reading = frappe.get_list("Pre Purchase Order Item",
                                                fields=["item_code", "want_to_purchase", "supplier", "price"],
                                               filters = {
                                                       "name": self.pre_purchase_order_item
                                               })

                frappe.set_value("Pre Purchase Order Item",self.pre_purchase_order_item,"item_code", 			self.item_code)

		frappe.set_value("Pre Purchase Order Item",self.pre_purchase_order_item,"want_to_purchase", 			self.want_to_purchase)

		frappe.set_value("Pre Purchase Order Item",self.pre_purchase_order_item,"supplier", 			self.supplier)

		frappe.set_value("Pre Purchase Order Item",self.pre_purchase_order_item,"price", 			self.price)

