import { useState } from "react";
export default function Accordion() {
  const [openedOnes, setOpenedOnes] = useState(new Set());

  const handleToggle = (id) => {
    const next = new Set(openedOnes);
    if (next.has(id)) {
      next.delete(id);
    } else {
      next.add(id);
    }
    setOpenedOnes(next);
  };
  return (
    <div>
      <div>
        <button onClick={() => handleToggle("html")} className="accordion-title" aria-expanded={openedOnes?.has("html")}>
          HTML{" "}
          <span
            aria-hidden={true}
            className={`accordion-icon ${openedOnes?.has("html") ? "accordion-icon--rotated" : ""}`}
          />
        </button>
        {openedOnes?.has("html") ? (
          <div className="content">
            The HyperText Markup Language or HTML is the standard markup
            language for documents designed to be displayed in a web browser.
          </div>
        ) : null}
      </div>
      <div>
        <button onClick={() => handleToggle("css")} className="accordion-title" aria-expanded={openedOnes?.has("css")}>
          CSS{" "}
          <span
            aria-hidden={true}
            className={`accordion-icon ${openedOnes?.has("css") ? "accordion-icon--rotated" : ""}`}
          />
        </button>
        {openedOnes?.has("css") ? (
          <div className="content">
            Cascading Style Sheets is a style sheet language used for describing
            the presentation of a document written in a markup language such as
            HTML or XML.
          </div>
        ) : null}
      </div>
      <div>
        <button onClick={() => handleToggle("js")} className="accordion-title" aria-expanded={openedOnes?.has("js")}>
          JavaScript{" "}
          <span
            aria-hidden={true}
            className={`accordion-icon ${openedOnes?.has("js") ? "accordion-icon--rotated" : ""}`}
          />
        </button>
        {openedOnes?.has("js") ? (
          <div className="content">
            JavaScript, often abbreviated as JS, is a programming language that
            is one of the core technologies of the World Wide Web, alongside
            HTML and CSS.
          </div>
        ) : null}
      </div>
    </div>
  );
}
