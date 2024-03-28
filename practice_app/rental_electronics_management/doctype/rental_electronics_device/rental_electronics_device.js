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

	refresh:function(frm){
	var curr_time=frappe.datetime.now_datetime().split('.')[0]
	if(curr_time>frm.doc.rented_until){
		frm.set_value('status','Available')
		frm.set_value('rented_until','')	
		cur_frm.save()
	}	
	}
})


