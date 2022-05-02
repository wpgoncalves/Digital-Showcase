django.jQuery(document).ready(function() {
    // Aplica máscara ao campo de formulário (CNPJ).
    django.jQuery(".vMaskCnpjField").mask("00.000.000/0000-00", {reverse: true});
    
    // Aplica máscara ao campo da lista para visualização (CNPJ).
    django.jQuery("td[class='field-cnpj']").attr("class", "field-cnpj vMaskCnpjTh");
    django.jQuery(".vMaskCnpjTh").mask("00.000.000/0000-00", {reverse: true});

    // Ao submeter o formulário para salvamento das informações é retirada a máscara dos valores dos campos.
    django.jQuery("#stores_form").submit(function() {
        django.jQuery(this).find(":input[class*='vMask']").unmask();
    });
});