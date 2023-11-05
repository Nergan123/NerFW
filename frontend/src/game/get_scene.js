import Character from "./character";
import Choice from "./choice";

function GetScene(scene, HandleSceneSet) {
    console.log("triggered")
    console.log(scene)

    
    function compile_choice(choiceData, HandleSceneSet){
        if (choiceData['options'] != null){
            const output = Choice(choiceData, HandleSceneSet);
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
                compile_choice(scene['choice'], HandleSceneSet)
            }
        </div>
    )
}


// "{\"line\": \"\"\054 \"back\": false\054 \"choices\": {}}"

export default GetScene;