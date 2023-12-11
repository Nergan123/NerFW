import { useState, useEffect } from "react";


function AudioGroup({sourcesInput}){

    console.log(sourcesInput)

    const [sources, setSources] = useState([]);
    const initialState = new Array(sources.length).fill(false);
    const [playing, setPlaying] = useState(initialState)
    const handldEnded = () => setPlaying(false);

    function handleSources(){

        const processedSources = [...sources];
        sourcesInput.map((source) =>{
                var loc = window.location.href;
                loc = loc.replace("game", source);
                const idx = sources.findIndex(e => e.source === loc);
                if(idx <= -1){
                    const audio = {
                        source: loc,
                        player: new Audio(),
                    }
                    audio.player.src = loc;
                    audio.player.type = "audio/mp3";
                    audio.player.load();
                    audio.player.play();
                    audio.player.addEventListener('ended', handldEnded, false);
                    processedSources.push(audio);
                }
                return source;
            }
        );
        setSources(processedSources);
    };

    function stopMusic(){
        const processedSources = sources.map((audio) => {
            return audio.player.pause();
        });
        setSources(processedSources)
        console.log("Sources ", sources)
    }

    useEffect(() => {
        sources.map((source, idx) =>{
            const filler = [...playing];
            filler[idx] = false
            source.player.addEventListener('ended', () => setPlaying(filler));
        })
        
        return () => {
            sources.map((source, idx) => {
                const filler = [...playing];
                filler[idx] = false
                source.player.removeEventListener('ended', () => setPlaying(filler));
                source.player.pause()
            })
        };
      }, [sources]);

    return(
        <div>
            <button onClick={handleSources}>Enable sound</button>
        </div>
    );

}


export default AudioGroup;