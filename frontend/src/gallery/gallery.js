import { useEffect, useState } from 'react';


function Gallery() {

    const [images, setImages] = useState([]);
    const [categories, setCategories] = useState([]);

    useEffect(() => {
        console.log("Fetching")
        const fetchImages = async () => {
            const response = await fetch('/gallery', {
                method: 'GET'
            });
    
            const data = await response.json();
            console.log(data);
            setImages(data.map((image) => {
                return <img src={`data:image/jpeg;base64,${image.image}`} />
                })
            );
        }

        fetchImages();
    }, []);

    return (
        <div>
            {images.map((image, idx) => {
                return <div key={idx}>{image}</div>
            })}
        </div>
    );
}


export default Gallery;