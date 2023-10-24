import { Route, Routes} from "react-router-dom";
import RouteGuard from "./route_guard.js";
import Game from "../game/game.js";
import Home from "../home/home.js";
import Login from "../login/login.js";


function RoutesHome() {
    return (
        <Routes>
            <Route exact path='/' element={<RouteGuard />}>
                <Route exact path="/" element={<Home />} />
            </Route>
            <Route exact path='/game' element={<RouteGuard />}>
                <Route exact path="/game" element={<Game />} />
            </Route>
            <Route exact path="/Login" element={<Login />} />
        </Routes>
    );
}

export default RoutesHome;
