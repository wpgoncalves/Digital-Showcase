django.jQuery(document).ready(function() {
    // Apply mask to form field (CNPJ)
    django.jQuery(".vMaskCnpjField").mask("00.000.000/0000-00", {reverse: true});
    
    // Applies mask to the list field for viewing (CNPJ).
    django.jQuery("td[class='field-cnpj']").attr("class", "field-cnpj vMaskCnpjTh");
    django.jQuery(".vMaskCnpjTh").mask("00.000.000/0000-00", {reverse: true});

    // When submitting the form to save the information, the mask from the field values is removed.
    django.jQuery("#stores_form").submit(function() {
        django.jQuery(this).find(":input[class*='vMask']").unmask();
    });
});