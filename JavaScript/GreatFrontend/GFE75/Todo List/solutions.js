import { useState } from "react";

export default function App() {
  const [items, setItems] = useState([]);
  const [value, setValue] = useState("");
  console.log(items)

  const addItem = () => {
      if (value) {
        const key = Date.now();
        setItems([
          ...items,
          {
            key,
            value:value.trim(),
          },
        ]);
        setValue("")
      } else {
        alert("Add some task");
      }

  };

  const deleteItem = (key) => {
    const filteredItems = items.filter((item) => item.key !== key);
    setItems(filteredItems);
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
        />
        <div>
          <button onClick={addItem}>Submit</button>
        </div>
      </div>
      <ul>
        {items.map((item) => (
          <li key={item.key}>
            <span>{item.value}</span>
            <button onClick={() => deleteItem(item.key)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
