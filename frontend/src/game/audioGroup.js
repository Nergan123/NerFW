import { useState, useEffect, useRef } from "react";


function AudioGroup({sourcesInput}){

    const [sources, setSources] = useState([]);
    const initialState = new Array(sources.length).fill(false);
    const [playing, setPlaying] = useState(initialState)

    const musicToStop = useRef();
    musicToStop.current = sources;

    function playOnRepeat(audio){
        console.log("Playing on repeat")
        audio.addEventListener('ended', () => {
            audio.currentTime = 0;
            audio.play();
        });
        audio.loop = true;
    }

    function checkSourceInList(){
        const links = sourcesInput.map((url) => {
            console.log(url.name)
            var loc = window.location.href;
            loc = loc.replace("game", url.name);
            return loc
        });
        const newSources = [...sources];
        sources.forEach((source, idxToDelete) => {
            const idx = links.findIndex(e => e === source.source);
            if(idx <= -1){
                const filler = [...playing];
                filler[idx] = false
                source.player.removeEventListener('ended', () => {});
                source.player.pause();
                newSources.splice(idxToDelete, 1);
            }
        });
        setSources(newSources);
    };

    function handleSources(){
        if(sourcesInput.length === 0 || sourcesInput.includes("")){
            return null
        }
        const processedSources = [...sources];
        sourcesInput.forEach((source) =>{
                var loc = window.location.href;
                loc = loc.replace("game", source.name);
                const idx = sources.findIndex(e => e.source === loc);
                if(idx <= -1 && !playing[idx]){
                    const audio = {
                        source: loc,
                        player: new Audio(),
                    }
                    if (source.repeatable){
                        playOnRepeat(audio.player);
                    }
                    audio.player.src = loc;
                    audio.player.type = "audio/mp3";
                    audio.player.load();
                    audio.player.play();
                    processedSources.push(audio);
                }
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