function GetScene(scene) {
    console.log("triggered")

    return(
        <div id="show-data">
            <p>{scene['text']}</p>
        </div>
    )
}


export default GetScene;