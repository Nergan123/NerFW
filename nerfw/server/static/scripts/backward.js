function BackwardFunction() {
    $.ajax({
        url: "/game/backward",
        type: "POST",
        data: {}
    }).done(function(response) {

        for (var element_id in response['html']){
            var value = response['html'][element_id];
            document.getElementById(element_id).innerHTML = value;
        }

        for (var element_id in response['css']){
            var value = response['css'][element_id]
            document.getElementById(element_id).style.cssText = value;
        };
    });
};