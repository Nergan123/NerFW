import React, { useState } from 'react';


function ImageSelected(props, idx) {

    const [selected, setSelected] = useState(false);

    function handleClick() {
        console.log("Image clicked");
        setSelected(!selected);
    }

    const styleNotSelected = {
        height: '15em',
        zIndex: 1,
    }

    const styleSelected = {
        position: 'absolute',
        top: 0,
        left: 0,
        height: `${window.innerHeight - 20}px`,
        zIndex: 2,
        backgroundColor: 'rgba(0, 0, 0, 0.75)',
    }

    const style = selected ? styleSelected : styleNotSelected;
    const imageSource = `data:image/jpeg;base64,${props.image.image}`;
    
    return (
        <div>
            <img className="ImageFrame" src={imageSource} onClick={handleClick} key={idx} style={style} />
            <p className="Title">{props.image.label}</p>
        </div>
    );
}


export default ImageSelected;