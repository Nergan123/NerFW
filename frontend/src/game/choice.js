function Choice(ChoiceData){

    return(
        <div className="big_wrapper">
            <div className="choice">
                {ChoiceData['options'].map((choice) => {
                    return <button className="button_specific" id={choice['id']} value={choice['text']}>{choice['text']}</button>
                }
                )}
            </div>
        </div>
    );

}


export default Choice