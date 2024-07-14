import React, { useState } from 'react';

function Cell({ initialValue, onSave }) {
    const [isEditing, setIsEditing] = useState(false);
    const [value, setValue] = useState(initialValue);

    const handleDoubleClick = () => {
        setIsEditing(true);
    };

    const handleChange = (e) => {
        setValue(e.target.value);
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            setIsEditing(false);
            onSave(value);
        }
    };

    const handleBlur = () => {
        setIsEditing(false);
        onSave(value);
    };

    return (
        <td
            className="rounded-xl border border-slate-300 hover:bg-stone-300"
            onDoubleClick={handleDoubleClick}
        >
            {isEditing ? (
                <input
                    type="text"
                    value={value}
                    onChange={handleChange}
                    onKeyDown={handleKeyDown}
                    onBlur={handleBlur}
                    autoFocus
                    className="w-full rounded-lg"
                />
            ) : (
                value
            )}
        </td>
    );
}

export default Cell;
