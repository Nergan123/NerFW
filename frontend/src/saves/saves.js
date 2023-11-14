import { useNavigate } from "react-router-dom";
import RenderVisualBackground from "./render_background";
import { useEffect, useState } from "react";


function Saves(){

    const [saves, setSaves] = useState([]);

    const navigate = useNavigate();

    function handleClick(){
        navigate('/')
    }

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
        <div style={{height: "100%"}}>
            <button onClick={handleClick}>main_menu</button>
            <div id="show-data">
                {saves.map((scene, idx) => {
                    const output = RenderVisualBackground(scene["data"], idx);
                    return(output)
                })}
            </div>
        </div>
    );
}


export default Saves;