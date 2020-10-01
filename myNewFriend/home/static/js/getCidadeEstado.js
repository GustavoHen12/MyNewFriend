$.getJSON('https://servicodados.ibge.gov.br/api/v1/localidades/estados/', {id: 10, }, function (json) {
    var options = '<option value="">...</option>';
    for (var i = 0; i < json.length; i++) {
        options += '<option data-id="' + json[i].id + '" value="' + json[i].nome + '" >' + json[i].nome + '</option>';
    }
    $("select[name='estado']").html(options);
});


$("select[name='estado']").change(function () {
    if ($(this).val()) {
        $.getJSON('https://servicodados.ibge.gov.br/api/v1/localidades/estados/'+$(this).find("option:selected").attr('data-id')+'/municipios', {id: $(this).find("option:selected").attr('data-id')}, function (json) {
            var options = '<option value="">...</option>';
            for (var i = 0; i < json.length; i++) {
                options += '<option value="' + json[i].nome + '" >' + json[i].nome + '</option>';
            }
            $("select[name='cidade']").html(options);
        });
    } else {
        $("select[name='cidade']").html('<option value="">...</option>');
    }
});

