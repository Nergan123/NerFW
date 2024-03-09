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
        const response = await fetch("/api/get_saves", {
            method: 'POST',
            redirect: 'follow',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({
                data: save
            })
           });

           if(response.status === 200){
            navigate("/game");
           };
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