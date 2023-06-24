function ForwardFunction() {
    $.ajax({
        url: "/game/forward",
        type: "POST",
        data: {}
    }).done(function(response) {
        document.getElementById("show-data").innerHTML = response['html'];
        for (var element_id in response['css']){
            var value = response['css'][element_id]
            document.getElementById(element_id).style.cssText = value;
        };
    });
};
