import './home.css'
import { useNavigate } from 'react-router-dom';


function Home() {

    const navigate = useNavigate();

    function handleClickToGame() {
        navigate("/game");
    }

    function handleClickToSaves() {
        navigate("/saves");
    }
    
    function handleClickToGallery() {
        navigate("/gallery");
    }

    return (
        <div id="main_menu" className="button_div">
            <button onClick={handleClickToGame}>Game</button>
            <button onClick={handleClickToSaves}>Saves</button>
            <button onClick={handleClickToGallery}>Gallery</button>
        </div>
    );
}


export default Home;
