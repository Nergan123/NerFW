import AudioGroup from "./audioGroup";
import Character from "./character";
import Choice from "./choice";

function GetScene(scene, HandleSceneSet) {

    
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
            <AudioGroup sourcesInput={[scene.audio]}/>
            {
                scene['characters'].map((character, idx) => {
                    return(<Character charData={character} idx={idx}/>)
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