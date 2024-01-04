import "../stylesheets/index.css"

function Character({charData, idx}){

    const charStyle = charData['css']

    return(
        <img
        id={charData['name']}
        src={`data:image/jpeg;base64,${charData['img']}`}
        alt="character"
        style={charStyle}
        key={idx}
        height={charData.scale.height + "px"}
        width={charData.scale.width + "px"}
        />
    );
}


export default Character;