import './home.css'
import { useNavigate } from 'react-router-dom';


function Home() {

    const navigate = useNavigate();

    function handleClick() {
        navigate("/Game");
    }

    return (
        <div id="main_menu" className="button_div">
            <button onClick={handleClick}>Game</button>
            <button >Saves</button>
        </div>
    );
}


export default Home;
