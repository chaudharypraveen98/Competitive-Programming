import { useEffect, useState } from "react";

export default function TrafficLight() {
  const [active, setActive] = useState(null);

  useEffect(() => {
    const interval = setInterval(() => {
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
            return "red";
        }
      });
    }, 2000);

    return () => {
      clearInterval(interval);
    };
  }, []);

  console.log("active", active);

  return (
    <div className="flex flex-row justify-center items-center">
      <div className="flex flex-col w-54 h-137 justify-between p-4 border border-border-card rounded-lg bg-bg-card">
        <div
          className={`h-full w-full flex-1 rounded-full ${active === "red" ? "bg-red-500" : "bg-slate-600"}`}
        ></div>
        <div
          className={`h-full w-full flex-1 rounded-full ${active === "yellow-down" || active === "yellow-up" ? "bg-yellow-400" : "bg-slate-600"}`}
        ></div>
        <div
          className={`h-full w-full flex-1 rounded-full ${active === "green" ? "bg-green-500" : "bg-slate-600"}`}
        ></div>
      </div>
    </div>
  );
}
