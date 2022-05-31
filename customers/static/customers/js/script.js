var vMaskPhoneBehavior = function(val) {
    return val.replace(/\D/g,"").length === 11 ? "(00) 00000-0000" : "(00) 0000-00009";
},
optPhone = {
    onKeyPress: function(val, e, field, options) {
        field.mask(vMaskPhoneBehavior.apply({}, arguments), options)
    }
};

var vMaskCpfCnpjBehavior = function() {
    return $("#kind option:selected").val() === "cpf" ? "000.000.000-00" : "00.000.000/0000-00";
},
optCpfCnpj = {
    onKeyPress: function(val, e, field, options) {
        field.mask(vMaskCpfCnpjBehavior.apply({}, arguments), options)
    }
};

$(document).ready(function() {
    $('#cpf_cnpj').mask(vMaskCpfCnpjBehavior, optCpfCnpj);
    $('#phone').mask(vMaskPhoneBehavior, optPhone);

    $("#kind").on("change", function() {
        $("#cpf_cnpj").val("")
    });

    $("#customers_form").submit(function() {
        $("#cpf_cnpj").unmask();
        $("#phone").unmask();
    });
});