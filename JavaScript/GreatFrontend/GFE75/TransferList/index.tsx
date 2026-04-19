import { useState } from "react";
import "./index.css";

type ListItem = {
    name: string;
    checked: boolean;
};

export default function TransferList() {
    function createObject(items: string[]) {
        return items?.map((item) => ({
            name: item,
            checked: false,
        }));
    }
    const [list1, setList1] = useState(
        createObject(["HTML", "JavaScript", "CSS", "TypeScript"]),
    );
    const [list2, setList2] = useState(
        createObject(["React", "Angular", "Vue", "Svelte"]),
    );

    const handleSelectChange = (
        itemName: string,
        checked: boolean,
        list1 = true,
    ) => {
        const updateCheckBox = (prev: ListItem[]) => {
            return prev.map((item) => {
                if (item.name !== itemName) {
                    return item;
                } else {
                    return {
                        ...item,
                        checked,
                    };
                }
            });
        };
        if (list1) {
            setList1((prev) => updateCheckBox(prev));
        } else {
            setList2((prev) => updateCheckBox(prev));
        }
    };

    const handleTransfer = (
        movement: "leftAll" | "left" | "right" | "rightAll",
    ) => {
        console.log("movement", movement);
        if (movement === "leftAll") {
            setList1((prev) => [...prev, ...list2]);
            setList2([]);
        } else if (movement === "left" || movement === "right") {
            const selectedItems: ListItem[] = [];
            const unSelectedItems: ListItem[] = [];
            const array = movement === "left" ? list2 : list1;
            array?.forEach((item) => {
                if (item.checked) {
                    selectedItems.push(item);
                } else {
                    unSelectedItems.push(item);
                }
            });
            if (movement === "left") {
                setList1((prev) => [...prev, ...selectedItems]);
                setList2(unSelectedItems);
            } else {
                setList1(unSelectedItems);
                setList2((prev) => [...prev, ...selectedItems]);
            }
        } else if (movement === "rightAll") {
            setList2((prev) => [...prev, ...list1]);
            setList1([]);
        }
    };
    const isList1Selected = list1.some(item => item.checked);
    const isList2Selected = list2.some(item => item.checked);
    return (
        <div>
            <div className="transferList__main_container">
                <ul>
                    {list1?.map((item) => {
                        return (
                            <li key={item.name}>
                                <input
                                    type="checkbox"
                                    checked={item?.checked}
                                    onChange={(e) =>
                                        handleSelectChange(
                                            item.name,
                                            e.target.checked,
                                        )
                                    }
                                />{" "}
                                {item.name}
                            </li>
                        );
                    })}
                </ul>
                <div className="transferList__divider">
                    <button
                        type="button"
                        className="transferList__btn"
                        onClick={() => handleTransfer("leftAll")}
                    >
                        {"<<"}
                    </button>
                    <button
                        type="button"
                        className="transferList__btn"
                        onClick={() => handleTransfer("left")}
                        disabled={!isList2Selected}
                    >
                        {"<"}
                    </button>
                    <button
                        type="button"
                        className="transferList__btn"
                        disabled={!isList1Selected}
                        onClick={() => handleTransfer("right")}
                    >
                        {">"}
                    </button>
                    <button
                        type="button"
                        className="transferList__btn"
                        onClick={() => handleTransfer("rightAll")}
                    >
                        {">>"}
                    </button>
                </div>
                <ul>
                    {list2?.map((item) => {
                        return (
                            <li key={item.name}>
                                <input
                                    type="checkbox"
                                    checked={item?.checked}
                                    onChange={(e) =>
                                        handleSelectChange(
                                            item.name,
                                            e.target.checked,
                                            false,
                                        )
                                    }
                                />{" "}
                                {item.name}
                            </li>
                        );
                    })}
                </ul>
            </div>
        </div>
    );
}
