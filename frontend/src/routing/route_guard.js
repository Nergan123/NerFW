import React from "react";
import { Outlet, Navigate } from 'react-router-dom';
import {Cookies} from "react-cookie";


const RouteGuard = () => {

    const cookie = new Cookies();

    const token = cookie.get("token");
    if (token !== undefined && token !== null && token !== "") {
        return <Outlet />;
    } else {
        return <Navigate to="/Login" />;
    }

}


export default RouteGuard;