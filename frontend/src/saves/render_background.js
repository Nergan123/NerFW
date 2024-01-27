import Character from "../game/character";


function RenderVisualBackground({scene, idx, state}){

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

    const buttons_container = {
        display: 'flex',
        flexFlow: 'row',
        margin: '10px 10px 10px 10px'
    }

    const wrapper_style = {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignSelf: 'flexEnd',
        width: '100%'
    }

    const charNameStyle = {
        fontSize: "20px",
        fontWeight: "bold",
        color: `rgb(${scene['color'][0]}, ${scene['color'][1]}, ${scene['color'][2]})`,
    }

    function getSceneText(){
        if (scene['choice']['options'] != null) {
            return "";
        }else if (scene['stringInput']['text'] != null){
            return "";
        }
        return scene['text'];
    }

    function getStyle(){
        if(state[idx]){
            return(backgroundStyleInvisible);
        }else{
            return(backgroundStyleVisible);
        }
    }

    return(
        <div className="Save" key={idx} style={getStyle()}>
            {scene['characters'].map((character, idx) => {
                return(<Character charData={character} idx={idx}/>)
            })}
            <div id="dialogue_menu">
                <div id="wrapper" style={wrapper_style}>
                <div style={buttons_container}>
                    <div id="back" className="button_div"><button>back</button></div>
                    <div id="next" className="button_div"><button>next</button></div>
                </div>
                <div style={buttons_container}>
                    <div id="main_menu" className="button_div"><button>main_menu</button></div>
                    <div id="save" className="button_div"><button>save</button></div>
                </div>
                </div>

                <form method="POST" style={{'margin': '10px 20px'}}>
                    <div id="char-name">
                        <p style={charNameStyle}>{scene.name}</p>
                    </div>
                    <div id="char-text">
                        <p>{getSceneText()}</p>
                    </div>
                </form>
            </div>
        </div>
    );
}


export default RenderVisualBackground;