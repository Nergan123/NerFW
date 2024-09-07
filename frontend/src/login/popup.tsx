import Button from "../utils/button";

function Popup({ setPopup, popupMessage }: { setPopup: (value: boolean) => void, popupMessage: string }) {
    return (
        <div className="fixed top-0 left-0 flex flex-col z-10 w-screen h-screen bg-black bg-opacity-10 backdrop-blur-sm items-center justify-center">
            <div className="flex flex-col bg-white bg-opacity-20 backdrop-blur-lg border-2 border-white p-5 rounded-2xl gap-3">
                <h1 className={"text-2xl text-white font-bold mb-3"}>Something went wrong</h1>
                <p className={"text-lg text-white"}>{popupMessage}</p>
                <Button onClick={() => setPopup(false)}>Close</Button>
            </div>
        </div>
    );
}

export default Popup;
