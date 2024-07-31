import "../stylesheets/index.css"
import pako from "pako";

function Character({charData, idx}) {

    const charStyle = charData['css']

    const compressedData = charData.img;
    const byteArray = Uint8Array.from(atob(compressedData), (c) => c.charCodeAt(0));
    const decompressedData = pako.inflate(byteArray, {to: 'string'});


    return (
        <img
            id={charData['name']}
            src={`data:image/jpeg;base64,${decompressedData}`}
            alt="character"
            style={charStyle}
            key={idx}
            height={charData.scale.height}
            width={charData.scale.width}
        />
    );
}


export default Character;