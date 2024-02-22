import React from "react";
import { Outlet, Navigate } from 'react-router-dom';
import {Cookies} from "react-cookie";


const RouteGuard = () => {

    const cookie = new Cookies();

    return cookie.get("token") ? <Outlet /> : <Navigate to="/Login" />;

}


export default RouteGuard;