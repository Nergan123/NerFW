function ImageSelected(props, idx) {

    function handleClick() {
        console.log("Image clicked");
    }

    const style = {
        height: '15em',
    }

    return (
        <div>
            <div className="ImageFrame" key={idx}>
                <img src={`data:image/jpeg;base64,${props.image.image}`} onClick={handleClick} key={idx} style={style} />
            </div>
            <p className="Title">{props.image.label}</p>
        </div>
    );
}


export default ImageSelected;