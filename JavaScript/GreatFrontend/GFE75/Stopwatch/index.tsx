import { useEffect, useRef, useState } from "react";
import "./index.css";

export default function Stopwatch() {
    const [currentTimeStamp, setCurrentTimeStamp] = useState(0);
    const ref = useRef<number | null>(null);
    const [paused, setPaused] = useState(true);

    const handleTimer = (play = true) => {
        if (play) {
             setPaused(false)
            const timer = setInterval(() => {
                setCurrentTimeStamp((prev) => prev + 10);
            }, 10);
            ref.current = timer;
        } else {
            setPaused(true)
            if (ref.current) {
                clearInterval(ref.current);
            }
            ref.current = null;
        }
    };

    const resetTimer = () => {
        setPaused(true)
        if (ref.current) {
            clearInterval(ref.current);
            ref.current = null;
        }

        setCurrentTimeStamp(0);
    };

    const formatTime=(time: number)=>{
        const second = Math.floor((time/1000)%60);
        const minutes = Math.floor(time/60000);
        const milliseconds = Math.floor((time%1000)/10)
        return `${minutes.toString().padStart(2,"0")}m : ${second.toString().padStart(2,"0")}s.${milliseconds.toString().padStart(2,"0")}ms`
    }

    useEffect(() => {
      return () => {
        if(ref.current){
            clearInterval(ref.current)
        }
      }
    }, [])
    

    return (
        <div>
            <p>{formatTime(currentTimeStamp)}</p>
            <div className="stopwatch__container">
                <button
                    type="button"
                    onClick={() => handleTimer(ref.current ? false : true)}
                    className="stopwatch__btn"
                >
                    {paused  ?"Start": "Stop"}
                </button>
                <button
                    type="button"
                    onClick={resetTimer}
                    className="stopwatch__btn"
                >
                    Reset
                </button>
            </div>
        </div>
    );
}
