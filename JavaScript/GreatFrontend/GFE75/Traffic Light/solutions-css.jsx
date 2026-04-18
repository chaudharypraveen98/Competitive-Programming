import { useEffect, useState } from "react";
import "./traffic-light.css";

const colorTimeouts = {
  red: 4000,
  "yellow-up": 500,
  "yellow-down": 500,
  green: 3000,
};

export default function TrafficLight() {
  const [active, setActive] = useState("green");

  useEffect(() => {
    const timer = setTimeout(() => {
      setActive((prev) => {
        switch (prev) {
          case "red":
            return "yellow-down";
          case "yellow-down":
            return "green";
          case "yellow-up":
            return "red";
          case "green":
            return "yellow-up";
          default:
            return "green";
        }
      });
    }, colorTimeouts[active] || 2000);

    return () => {
      clearTimeout(timer);
    };
  }, [active]);

  return (
    <div className="traffic-light-container">
      <div className="traffic-light">
        <div
          className={`light red ${active === "red" ? "active" : "inactive"}`}
        ></div>
        <div
          className={`light yellow ${active === "yellow-down" || active === "yellow-up" ? "active" : "inactive"}`}
        ></div>
        <div
          className={`light green ${active === "green" ? "active" : "inactive"}`}
        ></div>
      </div>
    </div>
  );
}