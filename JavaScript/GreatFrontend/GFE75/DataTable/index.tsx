import { useState, useEffect } from "react";
import users from "./user";
import "./index.css"

export default function DataTable() {
  const [message, setMessage] = useState("Data Table");
  const [offset, setOffset] = useState(20);
  const [page, setPage] = useState(0);
  const totalPage = Math.ceil(users.length / offset);
  const slicedUsers = users?.slice(page * offset, page * offset + offset);

  const handleSizeChange = (e) => {
    setOffset(parseInt(e.target.value));
    setPage(0);
  };
  return (
    <div>
      <h1>{message}</h1>
      <table>
        <thead>
          <tr>
            {[
              { label: "ID", key: "id" },
              { label: "Name", key: "name" },
              { label: "Age", key: "age" },
              { label: "Occupation", key: "occupation" },
            ].map(({ label, key }) => (
              <th key={key}>{label}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {slicedUsers.map(({ id, name, age, occupation }) => (
            <tr key={id}>
              <td>{id}</td>
              <td>{name}</td>
              <td>{age}</td>
              <td>{occupation}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="pagination-container">
        <label htmlFor="offset-select">Rows per page:</label>
        <select id="offset" onChange={handleSizeChange} value={offset}>
          <option value="5">Show 5</option>
          <option value="10">Show 10</option>
          <option value="20">Show 20</option>
        </select>

        <button
          type="button"
          aria-label="Prev Button"
          disabled={page === 0}
          onClick={() => setPage((prev) => prev - 1)}
        >
          Prev
        </button>
        <span aria-live="polite">
          Page {page + 1} out of {totalPage}
        </span>
        <button
          type="button"
          aria-label="Next Button"
          onClick={() => setPage((prev) => prev + 1)}
          disabled={page + 1 == totalPage}
        >
          Next
        </button>
      </div>
    </div>
  );
}
