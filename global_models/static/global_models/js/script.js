var vMaskPhoneBehavior = function(val) {
    return val.replace(/\D/g,"").length === 11 ? "(00) 00000-0000" : "(00) 0000-00009";
},
optPhone = {
    onKeyPress: function(val, e, field, options) {
        field.mask(vMaskPhoneBehavior.apply({}, arguments), options)
    }
};

django.jQuery(document).ready(function() {
    django.jQuery('#id_number').mask(vMaskPhoneBehavior, optPhone);

    django.jQuery("#phones_form").submit(function() {
        django.jQuery("#id_number").unmask();
    });
});