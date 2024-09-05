import React from "react";

function Button(props: { children: React.ReactNode, className?: string, [key: string]: any }) {

    const {children, className, ...otherProps} = props;

    const classNameOriginal = "bg-white backdrop-blur-lg bg-opacity-5 " +
        "hover:bg-opacity-20 p-2 transition-all ease-in-out " +
        "duration-300 rounded border-[0.1rem] border-white text-white";

    return (
        <button className={`${classNameOriginal} ${className || ''}`} {...otherProps}>
            {children}
        </button>
    );
}

export default Button;
