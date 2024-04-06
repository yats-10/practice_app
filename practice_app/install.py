from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe import _

def after_install():
	create_item_custom_fields()

def create_item_custom_fields():
	create_custom_fields(
		{
			"Item": [
				{
					"label": _("Is Rental Electronics Device"),
					"fieldname": "is_rental_electronics_device",
					"fieldtype": "Check",
					"default": "0",
					"insert_after": "has_variants",
				},
				{
					"label": _("Rental Electronic Deevice"),
					"fieldname": "rental_electronic_device",
					"fieldtype": "Link",
					"options": "Rental Electronics Device",
					"insert_after": "is_rental_electronics_device",
					"hidden":1
				}
			]
		}
		
	)
	print("Custom Fields Created")
