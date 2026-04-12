import { useState } from "react";
import ModalDialog from "./ModalDialog";
import "./index.css"

export default function Modal() {
  const [title, setTitle] = useState("Modal Dialog");
  const [isOpened, setIsOpened] = useState(false);

  return (
    <div>
      <button
        type="button"
        aria-label="Toggle Modal"
        onClick={() => setIsOpened(true)}
      >
        Open Modal
      </button>
      {isOpened ? (
        <ModalDialog title={title} onClose={() => setIsOpened(false)}>
          One morning, when Gregor Samsa woke from troubled dreams, he found
          himself transformed in his bed into a horrible vermin. He lay on his
          armour-like back, and if he lifted his head a little he could see his
          brown belly, slightly domed and divided by arches into stiff sections.
        </ModalDialog>
      ) : null}
    </div>
  );
}
