function PassFunction() {
    var values = {};
    $.each($('form').serializeArray(), function(i, field) {
        values[field.name] = field.value;
    });

    if (values['Password'] != values['Repeat_password']){
        $("form").submit(function (e) {
            FailedPass();
            return false;
        });
    } else {
        $("form").submit(function (e) {
            return values;
        });
    }

}


function FailedPass() {
    document.getElementById("inner_popup").innerHTML = "<p>Passwords should match</p>";
    document.getElementById("popup").style.display = "flex";
    $("#popup").show();
}


function HidePopup(){
    document.getElementById("popup").style.display = "none";
}
