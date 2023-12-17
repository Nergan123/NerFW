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
                        <p><b>{scene.name}</b></p>
                    </div>
                    <div id="char-text">
                        <p>{scene.text}</p>
                    </div>
                </form>
            </div>
        </div>
    );
}


export default RenderVisualBackground;