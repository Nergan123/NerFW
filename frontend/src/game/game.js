import './choices.css'
import './dialogue_menu.css'
import { useNavigate } from 'react-router-dom';


function Game() {

    const navigate = useNavigate();

    function handleClick() {
        navigate("/");
    }

    const wrapper_style = {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignSelf: 'flexEnd',
        width: '100%'
    }

    const buttons_container = {
        display: 'flex',
        flexFlow: 'row',
        margin: '10px 10px 10px 10px'
    }

    function forwardClick() {
        let showData = document.getElementById("show-data")
        var data = fetch("/game/forward")
        showData.innerHTML = data
    }

    return(
        <div id="body_element">
            <div id="show-data">

            </div>
            <div className="button_div"><button onClick="PlayAudio('')">Enable sound</button></div>
            <div id="dialogue_menu">
                <div id="wrapper" style={wrapper_style}>
                <div style={buttons_container}>
                    <div id="back" className="button_div"><button onClick="BackwardFunction()">back</button></div>
                    <div id="next" className="button_div"><button onClick={forwardClick}>next</button></div>
                </div>
                <div style={buttons_container}>
                    <div id="main_menu" className="button_div"><button onClick={handleClick}>main_menu</button></div>
                    <div id="save" className="button_div"><button onClick="SaveFunction()">save</button></div>
                </div>
                </div>

                <form method="POST" style={{'margin': '10px 20px'}}>
                    <div id="char-name">

                    </div>
                    <div id="char-text">

                    </div>
                </form>
            </div>

        </div>
    );
}

export default Game;