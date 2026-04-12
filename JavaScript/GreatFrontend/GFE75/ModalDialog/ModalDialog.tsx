import { createPortal } from "react-dom";
import { useEffect, useId } from "react";

export default function ModalDialog({ children, title, onClose }) {
  const titleId = useId();
  useEffect(() => {
    const handleEsc = (e) => {
      if (e.key === "Escape") onClose();
    };
    window.addEventListener("keydown", handleEsc);
    document.body.style.overflow = "hidden";
    return () => {
      document.body.style.overflow = "unset";
      window.removeEventListener("keydown", handleEsc);
    };
  }, [onClose]);
  return createPortal(
    <div className="modal-container" onClick={onClose} role="presentation">
      <div
        className="modal-body"
        onClick={(e) => e.stopPropagation()}
        role="dialog"
        aria-modal="true"
        aria-labelledby={titleId}
      >
        <h1 id={titleId}>{title}</h1>
        {children}
        <div className="close-button">
          <button type="button" onClick={onClose} autoFocus>
            Close
          </button>
        </div>
      </div>
    </div>,
    document.body,
  );
}
