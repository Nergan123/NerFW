import Character from "./character";
import Choice from "./choice";

function GetScene(scene) {
    console.log("triggered")
    console.log(scene)

    function compile_choice(choiceData){
        if (choiceData['options'] != null){
            const output = Choice(choiceData);
            return output;
        } else {
            return null;
        }
        
    }

    return(
        <div id="show-data">
            {
                scene['characters'].map((character) => {
                    return(<Character charData={character} />)
                })
            }
            {
                compile_choice(scene['choice'])
            }
        </div>
    )
}


// "{\"line\": \"\"\054 \"back\": false\054 \"choices\": {}}"

export default GetScene;