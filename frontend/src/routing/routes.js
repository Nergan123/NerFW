import { Route, Routes} from "react-router-dom";
import RouteGuard from "./route_guard.js";
import Game from "../game/game.js";
import Home from "../home/home.js";
import Login from "../login/login.js";
import Register from "../register/register.js";
import Saves from "../saves/saves.js";


function RoutesHome() {

    return (
        <Routes>
            <Route exact path='/' element={<RouteGuard />}>
                <Route exact path="/" element={<Home />} />
            </Route>
            <Route exact path='/game' element={<RouteGuard />}>
                <Route exact path="/game" element={<Game />} />
            </Route>
            <Route exact path='/saves' element={<RouteGuard />}>
                <Route exact path="/saves" element={<Saves />} />
            </Route>
            <Route exact path="/Login" element={<Login />} />
            <Route exact path="/Register" element={<Register />} />
        </Routes>
    );
}

export default RoutesHome;
