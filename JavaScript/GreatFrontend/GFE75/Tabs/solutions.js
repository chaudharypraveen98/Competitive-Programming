import { useState } from "react";

export default function Tabs() {
  const [activeTab, setActiveTab] = useState("HTML");
  const options = ["HTML", "CSS", "JavaScript"];

  const handleTabClick = (tab) => {
    setActiveTab(tab);
  };
  return (
    <div>
      <div role="tablist">
        {options?.map((tab) => (
          <button
            key={tab}
            role="tab"
            aria-selected={activeTab === tab}
            onClick={() => handleTabClick(tab)}
            className={`tab ${activeTab === tab ? "tab-active" : ""}`}
          >
            {tab}
          </button>
        ))}
      </div>
      <div>
        {activeTab === "HTML" ? (
          <p>
            The HyperText Markup Language or HTML is the standard markup
            language for documents designed to be displayed in a web browser.
          </p>
        ) : null}
        {activeTab === "CSS" ? (
          <p>
            Cascading Style Sheets is a style sheet language used for describing
            the presentation of a document written in a markup language such as
            HTML or XML.
          </p>
        ) : null}
        {activeTab === "JavaScript" ? (
          <p>
            JavaScript, often abbreviated as JS, is a programming language that
            is one of the core technologies of the World Wide Web, alongside
            HTML and CSS.
          </p>
        ) : null}
      </div>
    </div>
  );
}
