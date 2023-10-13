import { Route, Routes} from "react-router-dom";
import Game from "./game/game.js";
import Home from "./home/home.js";


function RoutesHome() {
    return (
        <Routes>
            <Route exact path="/" element={<Home />} />
            <Route exact path="/game" element={<Game />} />
        </Routes>
    );
}

export default RoutesHome;
