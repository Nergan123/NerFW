import { useState } from 'react';
import './choices.css'
import './dialogue_menu.css'
import { useNavigate } from 'react-router-dom';
import GetScene from './get_scene';


function Game() {

    const [scene, SetScene] = useState({
        background: "",
        characters: [],
        name: "",
        text: "",
        choice: {},
        audio: ""
    });

    const navigate = useNavigate();

    function handleClick() {
        navigate("/");
    }

    const wrapper_style = {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignSelf: 'flexEnd',
        width: '100%'
    }

    const buttons_container = {
        display: 'flex',
        flexFlow: 'row',
        margin: '10px 10px 10px 10px'
    }

    const backgroundStyle = {
        height: "100%",
        backgroundImage: `url(data:image/jpeg;base64,${scene['background']}`,
        backgroundRepeat: "no-repeat",
        backgroundSize: "cover",
        backgroundPosition: "center",
    }

    function HandleSceneSet(data){
        SetScene(data);
    }

    async function forwardClick() {
        const data = await fetch("/game/forward", {
            method: 'POST',
            redirect: 'follow',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({
            })
           });
           
        if (data.redirected){
            window.location.href = data.url;
        }

        let dataStr = await data.json()
        HandleSceneSet(dataStr);
    }

    async function backwardClick() {
        const data = await fetch("/game/backward", {
            method: 'POST',
            redirect: 'follow',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({
            })
           });

        if (data.redirected){
            window.location.href = data.url;
        }
        
        let dataStr = await data.json()
        HandleSceneSet(dataStr);
    }

    async function SaveGame(){
        await fetch('game/save', {
            method: 'POST',
        })
    }

    return(
        <div id="body_element" style={backgroundStyle}>
            <div className="button_div"><button onClick="PlayAudio('')">Enable sound</button></div>
            {GetScene(scene, HandleSceneSet)}
            <div id="dialogue_menu">
                <div id="wrapper" style={wrapper_style}>
                <div style={buttons_container}>
                    <div id="back" className="button_div"><button onClick={backwardClick}>back</button></div>
                    <div id="next" className="button_div"><button onClick={forwardClick}>next</button></div>
                </div>
                <div style={buttons_container}>
                    <div id="main_menu" className="button_div"><button onClick={handleClick}>main_menu</button></div>
                    <div id="save" className="button_div"><button onClick={SaveGame}>save</button></div>
                </div>
                </div>

                <form method="POST" style={{'margin': '10px 20px'}}>
                    <div id="char-name">
                        <p><b>{scene['name']}</b></p>
                    </div>
                    <div id="char-text">
                        <p>{scene['text']}</p>
                    </div>
                </form>
            </div>

        </div>
    );
}

export default Game;