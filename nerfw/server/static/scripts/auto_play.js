function PlayAudio(input_src = "") {
    console.log(input_src)
    var elements = document.getElementsByClassName("my_audio");
    for (var element_id in elements){
        if (elements[element_id].nodeName == "AUDIO" ){

            var reg = new RegExp("src='(.+?)'");
            matches = input_src.match(reg);

            var searching_in = $(elements[element_id]).children('source')[0].src;
            if (matches !== null){
                if (searching_in.indexOf(matches[1])>-1){
                    return false;
                }
            }

            elements[element_id].load();
            var playPromise = elements[element_id].play();
            if (playPromise !== undefined) {
                playPromise.then(_ => {
                  console.log("playing");
                })
                .catch(error => {
                  console.log("not playing");
                });
            }
        }
    }
};
