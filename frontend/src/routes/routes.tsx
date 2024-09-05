import React from "react";
import {Route, Routes} from "react-router-dom";
import RouteGuard from "./routeGuard";
import Home from "../home/home";
import Login from "../login/login";
import Register from "../register/register";

function RoutesHome() {
    return (
        <Routes>
            <Route path="/" element={<RouteGuard />}>
                <Route path="/" element={<Home />} />
            </Route>
            <Route path="Login" element={<Login />} />
            <Route path={"Register"} element={<Register />} />
        </Routes>
    );
}

export default RoutesHome;
