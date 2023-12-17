import { useState, useEffect, useRef } from "react";


function AudioGroup({sourcesInput}){

    const [sources, setSources] = useState([]);
    const initialState = new Array(sources.length).fill(false);
    const [playing, setPlaying] = useState(initialState)

    const musicToStop = useRef();
    musicToStop.current = sources;

    function checkSourceInList(){
        const links = sourcesInput.map((url) => {
            var loc = window.location.href;
            loc = loc.replace("game", url);
            return loc
        });
        const newSources = [...sources];
        sources.map((source, idxToDelete) => {
            const idx = links.findIndex(e => e === source.source);
            if(idx <= -1){
                const filler = [...playing];
                filler[idx] = false
                source.player.removeEventListener('ended', () => setPlaying(filler));
                source.player.pause();
                newSources.splice(idxToDelete, 1);
            }
            return null
        });
        setSources(newSources);
    };

    function handleSources(){
        if(sourcesInput.length === 0 || sourcesInput.includes("")){
            return null
        }
        const processedSources = [...sources];
        sourcesInput.map((source) =>{
                var loc = window.location.href;
                loc = loc.replace("game", source);
                const idx = sources.findIndex(e => e.source === loc);
                if(idx <= -1 && !playing[idx]){
                    const audio = {
                        source: loc,
                        player: new Audio(),
                    }
                    audio.player.src = loc;
                    audio.player.type = "audio/mp3";
                    audio.player.load();
                    audio.player.play();
                    const filler = [...playing];
                    filler[idx] = true
                    audio.player.addEventListener('ended', () => setPlaying(filler));
                    processedSources.push(audio);
                }
                return source;
            }
        );
        setSources(processedSources);
    };

    useEffect(() => {
        if(sourcesInput.length > 0 && !sourcesInput.includes("")){
            console.log("Triggered");
            checkSourceInList();
            handleSources();
            musicToStop.current = sources;
        }
        console.log("Sources: ", sources);
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [sourcesInput]);

    useEffect(() => {
        sources.map((source, idx) =>{
            const filler = [...playing];
            filler[idx] = true
            source.player.addEventListener('ended', () => setPlaying(filler));
            return null;
        })
        
        return () => {
            console.log("Cleanup");
            const sources = musicToStop.current;
            sources.map((source, idx) => {
                console.log("Pausing audio: ", source);
                const filler = [...playing];
                filler[idx] = false
                source.player.removeEventListener('ended', () => setPlaying(filler));
                source.player.pause();

                return source;
            })
        };
        // eslint-disable-next-line react-hooks/exhaustive-deps
      }, []);

    return(
        <div>
            <button onClick={handleSources}>Enable sound</button>
        </div>
    );

}


export default AudioGroup;