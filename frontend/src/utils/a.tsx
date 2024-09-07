import React from "react";

function A(props: { children: React.ReactNode, className?: string, [key: string]: any }) {

    const {children, className, ...otherProps} = props;

    const classNameOriginal = "font-light text-white text-opacity-100 hover:text-opacity-80 transition-all ease-in-out duration-300 cursor-pointer";

    return (
        <a className={`${classNameOriginal} ${className || ''}`} {...otherProps}>
            {children}
        </a>
    );
}

export default A;
