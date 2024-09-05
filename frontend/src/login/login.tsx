import Button from "../utils/button";

function Login(){
    return (
        <div className={"flex flex-col w-screen h-screen justify-center items-center bg-gradient-to-br from-main to-secondary"}>
            <div className={"flex flex-col p-5 bg-opacity-5 bg-white backdrop-blur-lg rounded-2xl items-center gap-3"}>
                <h1 className={"text-4xl font-bold text-center text-white mb-3"}>Login</h1>
                <input className={"p-2 rounded bg-opacity-5 bg-white border-1 border-white text-white"} placeholder={"Username"}/>
                <input className={"p-2 rounded bg-opacity-5 bg-white border-1 border-white text-white"} placeholder={"Password"}/>
                <Button className={"w-full"}>Login</Button>
            </div>
        </div>
    );
}

export default Login;
