import { useEffect, useRef, useState } from "react";

type CheckboxItem = {
    id: string;
    name: string;
    checked: boolean | "indeterminate";
    children?: CheckboxItem[];
    handleCheckboxChange: (id: string, checked: boolean) => void;
    index: number;
    isIndeterminate?: boolean | undefined;
};

const CheckboxItem = ({
    id,
    name,
    checked,
    children,
    handleCheckboxChange,
    index,
    isIndeterminate,
}: CheckboxItem) => {
    const ref = useRef(null);
    useEffect(() => {
        if (ref.current) {
            ref.current.indeterminate = isIndeterminate;
        }
    }, [isIndeterminate]);
    console.log("name", name, isIndeterminate);
    return (
        <div className="checkbox">
            <input
                type="checkbox"
                checked={checked}
                id={id}
                name={name}
                className="checkbox__input"
                onChange={(e) => handleCheckboxChange(id, e.target.checked)}
                ref={ref}
            />
            <label htmlFor={String(id)} className="checkbox__label">
                {name}
            </label>
            <div className="checkbox__children">
                {children?.map((checkbox) => (
                    <CheckboxItem
                        id={checkbox.id}
                        name={checkbox.name}
                        checked={checkbox.checked}
                        children={checkbox.children}
                        key={checkbox.id}
                        handleCheckboxChange={handleCheckboxChange}
                        index={index}
                        isIndeterminate={checkbox.isIndeterminate}
                    />
                ))}
            </div>
        </div>
    );
};

export default function Checkboxes({
    defaultCheckboxData,
}: Readonly<{
    defaultCheckboxData: ReadonlyArray<CheckboxItem>;
}>) {
    const [checkboxes, setCheckboxes] = useState(defaultCheckboxData);

    function updateAllChildren(children: CheckboxItem[]| undefined, checked: boolean):CheckboxItem[]| undefined {
        if (children) {
            return children?.map((item) => {
                return {
                    ...item,
                    checked,
                    children: updateAllChildren(item.children, checked),
                    isIndeterminate: false
                };
            });
        }
        return children;
    }
    function recursiveState(
        currentCheckboxes: CheckboxItem[],
        id: string,
        checked: boolean,
    ) {
        return currentCheckboxes?.map((item: CheckboxItem): CheckboxItem => {
            console.log(item, id)
            if (item.id === id) {
                return {
                    ...item,
                    checked: checked,
                    children: updateAllChildren(item.children, checked),
                    isIndeterminate: false,
                };
            }
            if (item.children) {
                const newChildren = recursiveState(item.children, id, checked);
                const isAllChecked = newChildren?.every((e) => e.checked);
                const isAllUnchecked = newChildren?.every(
                    (e) => !e.checked && !e.isIndeterminate,
                );
                return {
                    ...item,
                    checked: isAllChecked,
                    children: newChildren,
                    isIndeterminate: !isAllChecked && !isAllUnchecked,
                };
            }
            return item;
        });
    }
    const handleCheckboxChange = (id: string, checked: boolean) => {
        setCheckboxes((prev) => {
            const newValues = recursiveState(prev, id, checked);
            console.log(newValues);
            return newValues;
        });
    };

    return (
        <div>
            {checkboxes?.map((checkbox, index) => {
                return (
                    <CheckboxItem
                        id={checkbox.id}
                        name={checkbox.name}
                        checked={checkbox.checked}
                        children={checkbox.children}
                        key={checkbox.id}
                        handleCheckboxChange={handleCheckboxChange}
                        index={index}
                        isIndeterminate={checkbox?.isIndeterminate}
                    />
                );
            })}
        </div>
    );
}
