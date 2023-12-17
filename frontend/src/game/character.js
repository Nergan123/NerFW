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
        />
    );
}


export default Character;