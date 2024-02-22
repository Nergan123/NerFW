import { useEffect, useState } from 'react';
import './home.css'
import { useNavigate } from 'react-router-dom';
import {Cookies} from "react-cookie";


function Home() {

    const [type, setType] = useState('');
    const [backGround, setBackGround] = useState('');

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

    function handleLogOut() {
        const cookie = new Cookies();
        cookie.remove("token");
        cookie.remove("error");
        cookie.remove("line");
        cookie.remove("prev_line");
        cookie.remove("prev_scene");
        navigate("/login");
    }

    const screenStyle = {
        position: 'absolute',
        top: '0',
        width: '100%',
        height: '100%',
        backgroundSize: 'cover',
        backgroundPosition: "center",
    }
    screenStyle[type] = backGround;

    useEffect(() => {
        const fetchBackground = async () => {
            const response = await fetch('/background', {
                method: 'GET'
            });
    
            const data = await response.json();

            setType(data.background.type);
            setBackGround(data.background.data);
        }

        fetchBackground();
    }, [setBackGround]);

    return (
        <div className='MenuScreen' style={screenStyle}>
            <div id="main_menu" className="MainMenuButtons">
                <button onClick={handleClickToGame}>Game</button>
                <button onClick={handleClickToSaves}>Saves</button>
                <button onClick={handleClickToGallery}>Gallery</button>
            </div>
            <button className="LogOutButton" onClick={handleLogOut}>Log Out</button>
        </div>
    );
}


export default Home;
