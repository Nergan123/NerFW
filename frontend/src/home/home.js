import './home.css'
import { useNavigate } from 'react-router-dom';


function Home() {

    const navigate = useNavigate();

    function handleClickToGame() {
        navigate("/Game");
    }

    function handleClickToSaves() {
        navigate("/saves");
    }

    return (
        <div id="main_menu" className="button_div">
            <button onClick={handleClickToGame}>Game</button>
            <button onClick={handleClickToSaves}>Saves</button>
        </div>
    );
}


export default Home;
