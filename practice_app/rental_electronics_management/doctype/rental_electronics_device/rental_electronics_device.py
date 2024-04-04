# Copyright (c) 2024, Yatharth and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe.utils import today
from frappe.model.mapper import get_mapped_doc

class RentalElectronicsDevice(Document):

    def validate(self):
        self.new_sales_order()
        frappe.msgprint("New Sales Order Has Been Created")


    def new_sales_order(self):
        doc=frappe.new_doc('Sales Order')
        doc.customer=self.customer
        doc.append('items',{
            'item_code':self.stock_item,
            'delivery_date':today(),
            'qty':self.total_rented_hours,
            'rate':self.hourly_rent,
            'amount':self.total_rented_hours*self.hourly_rent
        })
        doc.insert()
        doc.save()
   