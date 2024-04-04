frappe.ui.form.on('Item', {
    is_rental_electronics_device: function(frm) {
        frm.toggle_display("rental_electronic_device", false);
        if (frm.doc.is_rental_electronics_device) {
            frm.toggle_display("rental_electronic_device", true);
            frm.set_value("stock_uom", "Hour");
            frm.set_value("is_stock_item", 0);
        } 
    }
})




