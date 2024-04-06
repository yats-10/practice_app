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
        # doc=frappe.new_doc('Sales Order')
        
        # doc.customer=self.customer
        # itemDoc=frappe.new_doc('Sales Order Item')
        # itemDoc.qty=self.total_rented_hours
        # itemDoc.delivery_date=today()
        # itemDoc.item_code=self.stock_item
        # itemDoc.gst_hsn_code="999512"
        # # doc.append('items',{
        #     'item_code':self.stock_item,
        #     'delivery_date':today(),
        #     'qty':self.total_rented_hours,
        #     'rate':self.hourly_rent,
        #     'amount':self.total_rented_hours*self.hourly_rent,
        #     'gst_hsn_code':"999512"
        # # })
        doc=frappe.get_doc({
            'doctype':'Sales Order',
            'customer':self.customer
        })
        doc.insert(ignore_mandatory=True,
                   ignore_permissions=True)
        
        doc.save()
   