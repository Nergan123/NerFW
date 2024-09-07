import { createContext, useState, useEffect } from "react";

const BackgroundContext = createContext<string>("");

const BackgroundProvider = ({ children }: any) => {
    const [backgroundImage, setBackgroundImage] = useState<string>("");

    useEffect(() => {
        fetch("/api/ui/background")
            .then(response => response.blob())
            .then(blob => URL.createObjectURL(blob))
            .then(url => setBackgroundImage(url))
            .catch(error => console.error("Error fetching background image:", error));
    }, []);

    return (
        <BackgroundContext.Provider value={backgroundImage}>
            {children}
        </BackgroundContext.Provider>
    );
};

export { BackgroundContext, BackgroundProvider };
