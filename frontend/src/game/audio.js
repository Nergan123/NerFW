import { useEffect, useState } from "react";


  const AudioPlayer = ({ url }) => {
    var loc = window.location.href;
    loc = loc.replace("game", url);

    const [audio] = useState(new Audio(loc));
    const [playing, setPlaying] = useState(false);

    var tempUrl = window.location.href
    tempUrl = tempUrl.replace("Game", "");
    if(!playing & loc !== tempUrl){
        audio.src = loc;
        audio.type = "audio/mp3";
        audio.load();
        audio.play();
        setPlaying(true);
    }else{
        audio.pause();
    }

    useEffect(() => {
      audio.addEventListener('ended', () => setPlaying(false));
      return () => {
        audio.removeEventListener('ended', () => setPlaying(false));
      };
    }, [audio]);

    useEffect(() => {
      return () => {
        setPlaying(false);
        audio.pause();
      }
      // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [])

    return (
      audio
    )
  };

export default AudioPlayer;