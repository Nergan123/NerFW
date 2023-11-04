import Character from "./character";

function GetScene(scene) {
    console.log("triggered")
    console.log(scene)

    return(
        <div id="show-data">
            {
                scene['characters'].map((character) => {
                    return(<Character charData={character} />)
                })
            }
        </div>
    )
}


// "{\"line\": \"\"\054 \"back\": false\054 \"choices\": {}}"

export default GetScene;