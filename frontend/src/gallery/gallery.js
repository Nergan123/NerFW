import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './gallery.css';
import ImageSelected from './imageSelected';


function Gallery() {

    const [images, setImages] = useState([]);
    const [categories, setCategories] = useState([]);
    const [selectedCategory, setSelectedCategory] = useState('');

    const navigate = useNavigate();

    function handleClickToMainMenu() {
        navigate("/");
    }

    function handleSetSelectedCategory(category) {
        setSelectedCategory(category);
    }

    function categoriesSelector() {
        const handleAllClick = () => handleSetSelectedCategory("All");
        return (
            <div className='CategorieSelector'>
                <button className='CategorieButton' onClick={handleAllClick}>All</button>
                {
                    categories.map((category, idx) => {
                        const handleClick = () => handleSetSelectedCategory(category);

                        return (
                            <button className='CategorieButton' onClick={handleClick} key={idx}>
                                {category}
                            </button>
                        );
                    })
                }
            </div>
        )
    }

    function getSelectedImages() {
        let selectedImages = [];
        if(selectedCategory === 'All') {
            selectedImages = images;
        } else {
            selectedImages = images.filter((image) => {
                return image.category === selectedCategory;
            });
        }

        return (
            selectedImages.map((image, idx) => {
                return (
                        <div className='ImageSelected' key={idx}>
                            <ImageSelected image={image} idx={idx} />
                        </div>
                    );
                }
            )
        )
    }

    useEffect(() => {
        const fetchImages = async () => {
            const response = await fetch('/gallery', {
                method: 'GET'
            });
    
            const data = await response.json();
            setImages(data.map((image) => {
                return image;
                })
            );

            const toInclude = [];

            data.forEach((image) => {
                if(!toInclude.includes(image.category)) {
                    toInclude.push(image.category);
                }
            });

            setCategories(toInclude);
        }

        fetchImages();
    }, []);

    return (
        <div className='GalleryWrapper'>
            {categoriesSelector()}
            <div className='GalleryImages'>
                <div className='ImagesInner'>
                    {getSelectedImages()}
                </div>
            </div>
            <div className='MainMenuButtonDiv'>
                <button onClick={handleClickToMainMenu}>Main Menu</button>
            </div>
        </div>
    );
}


export default Gallery;