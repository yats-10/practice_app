// Copyright (c) 2024, Yats and contributors
// For license information, please see license.txt


frappe.ui.form.on('Rental Electronics Device', {

	onload:function(frm){
		if(frm.doc.__islocal){
			frm.set_value('status','Available')
		}
	},

	category: function(frm) {
        var category = frm.doc.category
        var rates = {
            'PC': 100,       
            'Laptop': 150,   
            'Monitor': 50,   
            'Printer': 80,   
            'Projector': 120 
        };
        frm.set_value('hourly_rent', rates[category]);
        frm.set_df_property('hourly_rent', 'read_only', 1);
    },

	rented_until:function(frm){
		var hourDiff=frappe.datetime.get_hour_diff(frm.doc.rented_until,frappe.datetime.now_datetime().split('.')[0])
		frm.set_value('total_rented_hours', hourDiff);
        frm.set_df_property('total_rented_hours', 'read_only', 1);
	},

	refresh:function(frm){
	if(frappe.datetime.now_datetime().split('.')[0]>frm.doc.rented_until){
		frm.set_value('status','Available')
		frm.set_value('rented_until','')	
		cur_frm.save()
	}	
	}
	
})

