import { useState } from "react";
import { useNavigate } from "react-router-dom";
import SaveButton from "./save_button";
import RenderVisualBackground from "./render_background";


function BackPairs({saves}){

    const initialState = new Array(saves.length).fill(false);

    const [pairs, setPairs] = useState(initialState);

    const navigate = useNavigate();

    function handleClick(){
        navigate('/')
    }

    function getButton(buttonName, idx, save){
        return(<SaveButton name={buttonName} key={idx} idx={idx} state={pairs} setStateFunction={setPairs} save={save}/>);
    }

    function getBackground(dataFromSave, idx){
        return(<RenderVisualBackground scene={dataFromSave} key={idx} idx={idx} state={pairs}/>);
    }

    const containerStyle = {
        display: "flex",
        flexDirection: "row",
        height: "100%",
    }

    return(
        <div className="pairsContainer" style={containerStyle}>
            <div className="ButtonsDiv" style={{display: "flex", flexDirection: "collumn", justifyContent: "space-between"}}>
                <div className="SavesButtons">
                    {saves.map((scene, idx) => {
                        return(
                            getButton(scene.date, idx, scene.save)
                        );
                    })}
                </div>
                <div className="ToMainMenu">
                    <button onClick={handleClick} style={{zIndex: 1}}>main_menu</button>
                </div>
            </div>
            <div className="SavesScreenshots" style={{width: "100%", backgroundImage: "linear-gradient(to right, #282a36, rgba(1, 1, 1, 0))"}}>
                {saves.map((scene, idx) => {
                    return(getBackground(scene.data, idx))
                })}
            </div>
        </div>
    );
}


export default BackPairs;