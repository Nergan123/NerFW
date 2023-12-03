import { useEffect, useState } from "react";


  const AudioPlayer = ({ url }) => {
    var loc = window.location.href
    loc = loc.replace("Game", url)
    console.log(loc)

    const [audio] = useState(new Audio(loc));
    const [playing, setPlaying] = useState(false);

    function playSound(){
        var tempUrl = window.location.href
        tempUrl = tempUrl.replace("Game", "");
        console.log(tempUrl)
        if(!playing & loc !== tempUrl){
            audio.src = loc;
            audio.type = "audio/mp3";
            audio.load();
            audio.play();
            setPlaying(true);
        }else{
            audio.pause();
        }
        
    }
  
    useEffect(() => {
        audio.addEventListener('ended', () => setPlaying(false));
        return () => {
          audio.removeEventListener('ended', () => setPlaying(false));
        };
      }, [audio]);

    return (
      <div>
        <button onClick={playSound}>Enable sound</button>
      </div>
    );
  };

export default AudioPlayer;