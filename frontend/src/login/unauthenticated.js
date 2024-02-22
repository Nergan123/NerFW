import { useNavigate } from "react-router-dom";
import {Cookies} from "react-cookie";
import './unauthenticated.css'


function Unauthenticated() {

    const navigate = useNavigate();
    const cookie = new Cookies();

    function handleClickToLogin() {
        navigate("/login");
    }

    cookie.remove("error");

    return (
    <div className="unauthenticated">
        <h2>We were not able to authenticate you.</h2>
        <h2>Please contact the creator</h2>
        <h1>Sorry...</h1>
        <button className="button-unauth" onClick={handleClickToLogin}>
            Back To Login
        </button>
    </div>
    );
}


export default Unauthenticated;