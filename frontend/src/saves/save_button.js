import "./load_game.css"


function SaveButton({name, idx, state, setStateFunction}){

    function onMouseEntercustom(){
        console.log("changing true: ", idx);
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
        console.log("changing false: ", idx);
        const newState = new Array(state.length).fill(false);
        newState[idx] = false;
        setStateFunction(newState);
    };

    return(
        <button
        className="LoadSave"
        onMouseEnter={onMouseEntercustom}
        onMouseLeave={onMouseLeaveCustom}
        key={idx}
        >
            {name}
        </button>
    );
}


export default SaveButton;