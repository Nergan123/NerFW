function LoadSave(objButton) {
    $.ajax({
        url: "/game/load_game",
        type: "POST",
        data: {"data": objButton.value}
    }).done(function(response) {
        window.location.href = "/game";
        return response;
    });
};