import './stringInput.css';


function StringInput(name, idx, HandleSceneSet) {

    console.log(name);

    let inputName = "";

    const handleChange = (e) => {
        inputName = e.target.value;
    }

    async function submitStringInput(){
        const response = await fetch('/api/forward', {
            method: 'POST',
            redirect: 'follow',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify({
                "stringInput": inputName,
                "id": idx,
            })
           });
        let dataStr = await response.json()
        HandleSceneSet(dataStr);
    }

    return(
        <div className='big_wrapper'>
            <div className='stringInput'>
                <label>{name}</label>
                <input type="text" name={name} id={name} onChange={handleChange}/>
                <button className="button_specific" onClick={async () => await submitStringInput()}>Submit</button>
            </div>
        </div>
    )
}


export default StringInput;