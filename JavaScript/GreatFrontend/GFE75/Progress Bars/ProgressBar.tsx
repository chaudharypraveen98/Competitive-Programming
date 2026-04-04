import { useEffect, useState } from "react";
import "./styles.css";

const SingleBar = ({startFilling=false, transitionOver}) => {
	const [filling, setFilling] = useState(false);

	useEffect(() => {
	  if(startFilling){
		setFilling(true)
	  }
	}, [startFilling])
	
    return (
        <div className="bar-container">
            <div
                className="bar"
                style={{
                    width: filling ? "100%" :"0",
					transition:"width 2s linear"
                }}
				onTransitionEnd={transitionOver}
            ></div>
        </div>
    );
};
export default function ProgressBar() {
    const [filledBars, setFilledBars] = useState(0);
    const [requestedBars, setRequestedBars] = useState(0);

    const startBar = () => {
        setRequestedBars((prev) => prev + 1);
    };

	const handleTransitionOver=()=>{
		setFilledBars((prev)=>prev+1);

	}
    return (
        <div>
            <button onClick={startBar}>Add</button>
            {Array.from({ length: requestedBars }).map((_, index) => (
                <SingleBar  transitionOver={handleTransitionOver} startFilling={index===filledBars}/>
            ))}
        </div>
    );
}
