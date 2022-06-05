var vMaskCpfCnpjBehavior = function() {
    return django.jQuery("input[name='kind']:checked").val() === "Física" ? "000.000.000-00" : "00.000.000/0000-00";
},
optCpfCnpj = {
    onKeyPress: function(val, e, field, options) {
        field.mask(vMaskCpfCnpjBehavior.apply({}, arguments), options)
    }
};

django.jQuery(document).ready(function() {
    django.jQuery('#id_cpf_cnpj').mask(vMaskCpfCnpjBehavior, optCpfCnpj);

    django.jQuery("#id_kind").on("change", function() {
        django.jQuery("#id_cpf_cnpj").val("")
    });

    django.jQuery("#customers_form").submit(function() {
        django.jQuery("#id_cpf_cnpj").unmask();
    });
});