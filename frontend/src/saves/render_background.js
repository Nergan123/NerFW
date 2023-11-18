import Character from "../game/character";


function RenderVisualBackground({scene, idx, state}){

    console.log("received: ", state)
    console.log("My id: ", idx)

    const backgroundStyleVisible = {
        height: "100%",
        width: "100%",
        backgroundImage: `url(data:image/jpeg;base64,${scene['background']}`,
        backgroundRepeat: "no-repeat",
        backgroundSize: "cover",
        backgroundPosition: "center",
        zIndex: -1-idx,
        opacity: 0,
    }

    const backgroundStyleInvisible = {
        height: "100%",
        width: "100%",
        backgroundImage: `url(data:image/jpeg;base64,${scene['background']}`,
        backgroundRepeat: "no-repeat",
        backgroundSize: "cover",
        backgroundPosition: "center",
        zIndex: -1-idx,
        opacity: 1,
    }

    function getStyle(){
        if(state[idx]){
            console.log("Changing my style to true: ", idx);
            return(backgroundStyleInvisible);
        }else{
            console.log("Changing my style to false: ", idx);
            return(backgroundStyleVisible);
        }
    }

    return(
        <div className="Save" key={idx} style={getStyle()}>
            {scene['characters'].map((character, idx) => {
                return(<Character charData={character} idx={idx}/>)
            })}
        </div>
    );
}


export default RenderVisualBackground;