import { useEffect, useState } from 'react';
import './choices.css'
import './dialogue_menu.css'
import { useNavigate } from 'react-router-dom';
import GetScene from './get_scene';
import { useCookies } from 'react-cookie';


function Game() {

    const [cookie, setCookie] = useCookies(['line', 'prev_line', 'prev_scene']);

    const [scene, SetScene] = useState({
        background: "",
        characters: [],
        name: "",
        color: [],
        text: "",
        choice: {},
        stringInput: {},
        audio: ""
    });
    const [prevScene, SetPrevScene] = useState({
        background: "",
        characters: [],
        name: "",
        text: "",
        choice: {},
        stringInput: {},
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

    const charNameStyle = {
        fontSize: "20px",
        fontWeight: "bold",
        color: `rgb(${scene['color'][0]}, ${scene['color'][1]}, ${scene['color'][2]})`,
    }

    function HandleSceneSet(data){
        SetScene(data);
    }

    function HandlePrevSceneSet(data){
        SetPrevScene(data);
        setCookie('prev_scene', data);
    }

    async function forwardClick() {
        HandlePrevSceneSet(scene);
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
        await fetch("/game/backward", {
            method: 'POST',
            redirect: 'follow',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({
            })
        });
        SetScene(prevScene);
    }

    async function SaveGame(){
        await fetch('game/save', {
            method: 'POST',
        })
    }

    function getSceneText(){
        if (scene['choice']['options'] != null) {
            return "";
        }else if (scene['stringInput']['text'] != null){
            return "";
        }
        return scene['text'];
    }

    function getControlButtons(){
        if (scene['choice']['options'] != null || scene['stringInput']['text'] != null){
            return (
                <div></div>
            );
        }
        return (
            <div id="control_buttons" style={buttons_container}>
                <div id="back" className="button_div"><button onClick={backwardClick}>back</button></div>
                <div id="next" className="button_div"><button onClick={forwardClick}>next</button></div>
            </div>
        );
    
    }

    useEffect(() => {
        HandlePrevSceneSet(cookie.prev_scene);
        forwardClick();
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return(
        <div id="body_element" style={backgroundStyle}>
            {GetScene(scene, HandleSceneSet)}
            <div id="dialogue_menu">
                <div id="wrapper" style={wrapper_style}>
                {getControlButtons()}
                <div style={buttons_container}>
                    <div id="main_menu" className="button_div"><button onClick={handleClick}>main_menu</button></div>
                    <div id="save" className="button_div"><button onClick={SaveGame}>save</button></div>
                </div>
                </div>

                <form method="POST" style={{'margin': '10px 20px'}}>
                    <div id="char-name">
                        <p style={charNameStyle}>{scene['name']}</p>
                    </div>
                    <div id="char-text" style={{marginTop: "10px"}}>
                        <p>{getSceneText()}</p>
                    </div>
                </form>
            </div>

        </div>
    );
}

export default Game;