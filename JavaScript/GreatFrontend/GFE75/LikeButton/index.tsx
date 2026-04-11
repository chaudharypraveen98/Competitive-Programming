import { useState } from "react";
import { HeartIcon, SpinnerIcon } from "./icons";
import './index.css';

export default function LikeButton() {
  const [isLiked, setIsLiked] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [isHovered, setIsHovered] = useState(false);
  const [error, setError] = useState("");

  const handleClick = () => {
    setIsLoading(true);
    fetch("https://questions.greatfrontend.com/api/questions/like-button", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        action: isLiked ? "unlike" : "like",
      }),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error("Action Failed");
        } else {
          setIsLiked(!isLiked);
        }
      })
      .catch((error) => {
        console.log("failed", error.message);
        setError(error.message);
        setTimeout(() => {
          setError("");
        }, 1000);
      })
      .finally(() => {
        setIsLoading(false);
      });
  };
  return (
    <div>
      <button
        onClick={handleClick}
        type="button"
        aria-label="Toggle Like"
        aria-pressed={isLiked}
        disabled={isLoading}
        className={`btn-container ${isLiked ? "filled-state" : "default-state"}`}
      >
        {isLoading ? <SpinnerIcon /> : <HeartIcon />}
        {isLiked ? "Liked" : "Like"}
      </button>
      {error ? <p role="alert">{error}</p> : null}
    </div>
  );
}
