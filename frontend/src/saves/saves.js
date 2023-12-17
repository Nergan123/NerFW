import BackPairs from "./create_pairs";
import { useEffect, useState } from "react";
import "./saves_stacks.css"
import "./load_game.css"


function Saves(){

    const [saves, setSaves] = useState([]);

    const savesData = async () => {
        const response = await fetch('/game/load_game', {
            method: 'GET',
        });
        const responseData = await response.json();
        setSaves(responseData)
    }

    useEffect(() => {
        savesData()
    }, [])

    return(
        <div id="show-data" style={{height: "100%"}}>
            <BackPairs saves={saves} />
        </div>
    );
}


export default Saves;