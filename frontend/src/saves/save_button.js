import { useNavigate } from "react-router-dom";
import "./load_game.css"


function SaveButton({name, idx, save, state, setStateFunction}){
    const navigate = useNavigate();

    function onMouseEntercustom(){
        const newState = state.map((_, idOfVal) => {
            if(idOfVal === idx){
                return(true);
            }else{
                return(false);
            }
        });
        newState[idx] = true;
        setStateFunction(newState);
    };
    
    function onMouseLeaveCustom(){
        const newState = new Array(state.length).fill(false);
        newState[idx] = false;
        setStateFunction(newState);
    };

    async function HandleOnClick(){
        const response = await fetch("/game/load_game", {
            method: 'POST',
            redirect: 'follow',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({
                data: save
            })
           });

           const resp = await response.json()
           navigate(resp.url);
    }


    return(
        <button
        className="LoadSave"
        onMouseEnter={onMouseEntercustom}
        onMouseLeave={onMouseLeaveCustom}
        onClick={HandleOnClick}
        value={save}
        key={idx}
        >
            {name}
        </button>
    );
}


export default SaveButton;