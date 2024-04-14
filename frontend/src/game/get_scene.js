import AudioGroup from "./audioGroup";
import Character from "./character";
import Choice from "./choice";
import StringInput from "./stringInput";


function GetScene(scene, HandleSceneSet) {
    
    function compile_choice(choiceData, HandleSceneSet){
        if (choiceData['options'] != null){
            const output = Choice(choiceData, HandleSceneSet);
            return output;
        } else {
            return null;
        }
        
    }

    function getStringInput(inputFromScene, HandleSceneSet){
        if (inputFromScene['text'] != null){
            const output = StringInput(inputFromScene['text'], inputFromScene["id"], HandleSceneSet);
            return output;
        } else {
            return null;
        }
    }

    return(
        <div id="show-data" style={{position: "relative"}}>
            <AudioGroup sourcesInput={scene.audio}/>
            {
                scene['characters'].map((character, idx) => {
                    return(<Character charData={character} idx={idx}/>)
                })
            }
            {
                compile_choice(scene['choice'], HandleSceneSet)
            }
            {
                getStringInput(scene['stringInput'], HandleSceneSet)
            }
        </div>
    )
}

export default GetScene;