import { useState } from "react";

export default function App() {
  const [items, setItems] = useState([]);
  const [value, setValue] = useState("");
  const [editKey, setEditKey] = useState(null);
  const [editedText, setEditText] = useState("");
  console.log(items);

  const addItem = () => {
    const isItemExists = items.some((item) => item.value === value.trim());
    if (value.trim() && !isItemExists) {
      const key = Date.now();
      setItems((prev) => [
        ...prev,
        {
          key,
          value: value.trim(),
          checked: false,
        },
      ]);

      setValue("");
    } else if (isItemExists) {
      alert("duplicate task");
    } else {
      alert("add some desc");
    }
  };

  const saveEditedText = (key, value) => {
    const isItemExists = items.some((item) => item.key!==key && item.value === value.trim());
    if (!isItemExists) {
      setItems((prev) =>
        prev.map((item) =>
          item.key === key
            ? {
                ...item,
                value: value.trim(),
              }
            : item,
        ),
      );
      setEditText("");
      setEditKey(null);
    } else {
      alert("duplicate task");
    }
  };

  const toggleTodoItem = (key) => {
    // Because state updates are async and previous state may be stale.
    setItems((prev) =>
      prev.map((item) =>
        item.key === key
          ? {
              ...item,
              checked: !item.checked,
            }
          : item,
      ),
    );
  };

  const deleteItem = (key) => {
    const filteredItems = items.filter((item) => item.key !== key);
    setItems(filteredItems);
  };

  const deleteAll = () => {
    setItems([]);
  };

  return (
    <div>
      <h1>Todo List</h1>
      <div>
        <input
          type="text"
          placeholder="Add your task"
          id="add-input"
          value={value}
          onChange={(e) => {
            setValue(e.target.value);
          }}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              addItem();
            }
          }}
        />
        <div>
          <button onClick={addItem}>Submit</button>
        </div>
        <div>
          <button onClick={deleteAll}>deleteAll</button>
        </div>
      </div>
      <ul>
        {items.map((item) => (
          <li key={item.key}>
            <span
              style={{
                textDecoration: item?.checked ? "line-through" : "none",
              }}
            >
              {item.value}
            </span>
            <input
              name="completed-item"
              type="checkbox"
              checked={item.checked}
              onChange={() => toggleTodoItem(item.key)}
            />
            <button onClick={() => deleteItem(item.key)}>Delete</button>
            {item.key !== editKey ? (
              <button
                onClick={() => {
                  setEditKey(item.key);
                  setEditText(item.value);
                }}
              >
                Edit
              </button>
            ) : (
              <>
                <input
                  type="text"
                  value={editedText}
                  onChange={(e) => setEditText(e.target.value)}
                />
                <button onClick={() => saveEditedText(item.key, editedText)}>
                  Save
                </button>
                <button
                  onClick={() => {
                    setEditKey(null);
                    setEditText("");
                  }}
                >
                  Cancel
                </button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
