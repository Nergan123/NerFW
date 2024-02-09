function ImageSelected(image) {

    function handleClick() {
        console.log("Image clicked");
    }

    return (
    <div className="ImageFrame">
        <img src={`data:image/jpeg;base64,${image.image}`} onClick={handleClick} />
    </div>
    );
}


export default ImageSelected;