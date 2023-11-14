import Character from "../game/character";


function RenderVisualBackground(scene, key){

    console.log("Received a scene object: ", scene)

    function Background({imgSrc}){
        return(
            <img
            src={`data:image/jpeg;base64,${imgSrc}`}
            alt="background"
            style={{height: "100%"}}
            />
        );
    }

    return(
        <div className="save" key={key}>
            <Background imgSrc={scene["background"]} />
            {scene['characters'].map((character) => {
                return(<Character charData={character} />)
            })}
        </div>
    );
}


export default RenderVisualBackground;