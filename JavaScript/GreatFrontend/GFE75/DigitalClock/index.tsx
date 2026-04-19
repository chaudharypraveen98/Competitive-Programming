import { useEffect, useState } from "react";
import "./index.css";

const formatTime = (date) => {
    // Format your date here
    const formattedTime = date.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
    });
    return formattedTime;
};
export default function DigitalClock() {
    const [currentTimeStamp, setcurrentTimeStamp] = useState(
        formatTime(new Date()),
    );

    useEffect(() => {
        let timeout;
        const tick = () => {
            setcurrentTimeStamp(formatTime(new Date()));
            // this is useful for drift resistenace
            const delay = 1000 - (Date.now() % 1000);
            setTimeout(tick, delay);
        };
        timeout = setTimeout(tick, 1000 - (Date.now() % 1000));
        return () => {
            clearTimeout(timeout);
        };
    }, []);

    return <div className="clock__container">{currentTimeStamp}</div>;
}
