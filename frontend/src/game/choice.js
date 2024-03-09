function Choice(ChoiceData, HandleSceneSet){

    async function respond(buttonId, buttonValue){
        const response = await fetch('/api/forward', {
            method: 'POST',
            redirect: 'follow',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({
                "choice": buttonValue,
                "id": buttonId,
            })
           });
        let dataStr = await response.json()
        HandleSceneSet(dataStr);
    }

    return(
        <div className="big_wrapper">
            <div className="choice">
                {ChoiceData['options'].map((choice) => {
                    return <button className="button_specific"
                    id={choice['id']}
                    value={choice['text']}
                    onClick={async () => await respond(choice['id'], choice['text'])}>{choice['text']}</button>
                }
                )}
            </div>
        </div>
    );

}


export default Choice