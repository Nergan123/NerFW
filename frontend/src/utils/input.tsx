import React from "react";

function Input(props: { children?: React.ReactNode, className?: string, [key: string]: any }) {

    const {children, className, ...otherProps} = props;

    const classNameOriginal = "p-2 w-full rounded bg-opacity-5 bg-white border-1 " +
        "placeholder-white placeholder-opacity-55 border-white text-white " +
        "hover:bg-opacity-20 transition-all ease-in-out duration-300";

    return (
        <input className={`${classNameOriginal} ${className || ''}`} {...otherProps}>
            {children}
        </input>
    );
}

export default Input;
