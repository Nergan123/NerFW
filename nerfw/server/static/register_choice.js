function RegisterChoice(objButton) {
    $.ajax({
        url: "/game/forward",
        type: "POST",
        data: {"answer": objButton.value, "id": objButton.id}
    }).done(function(response) {
        for (var element_id in response['html']){
            var value = response['html'][element_id];
            document.getElementById(element_id).innerHTML = value;
        }

        for (var element_id in response['css']){
            var value = response['css'][element_id];
            document.getElementById(element_id).style.cssText = value;

        };
    });
};