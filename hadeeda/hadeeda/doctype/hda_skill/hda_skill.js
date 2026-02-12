// Copyright (c) 2024, Biz Technology Solutions and contributors
// For license information, please see license.txt

frappe.ui.form.on('HDA Skill', {
    refresh: function (frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__('Execute Skill'), function () {
                // Dialog to capture parameters
                let fields = [];
                if (frm.doc.parameters) {
                    frm.doc.parameters.forEach(param => {
                        fields.push({
                            label: param.parameter_name,
                            fieldname: param.parameter_name,
                            fieldtype: map_param_type(param.parameter_type),
                            reqd: param.is_required,
                            default: param.default_value
                        });
                    });
                }

                frappe.prompt(fields, values => {
                    frappe.call({
                        method: "hadeeda.hadeeda.controllers.skill_engine.execute_skill_endpoint",
                        args: {
                            skill_name: frm.doc.name,
                            params: values
                        },
                        callback: function (r) {
                            if (!r.exc) {
                                frappe.msgprint(__('Skill Executed. Result: ' + JSON.stringify(r.message)));
                            }
                        }
                    });
                }, __('Enter Parameters'), __('Execute'));
            });
        }
    }
});

function map_param_type(type) {
    const map = {
        'String': 'Data',
        'Integer': 'Int',
        'Float': 'Float',
        'Boolean': 'Check',
        'List': 'Small Text', // Simplified
        'Dict': 'Small Text' // Simplified
    };
    return map[type] || 'Data';
}
