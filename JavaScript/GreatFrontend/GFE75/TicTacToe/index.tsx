import { useMemo, useState } from "react";
import "./index.css";

const WINNING_LINES = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8], // Rows
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8], // Columns
    [0, 4, 8],
    [2, 4, 6], // Diagonals
];
export default function TicTacToe() {
    const [matrix, setMatrix] = useState(Array(9).fill(null));

    // 1. Derived State: Calculate winner and turn without extra useState
    const winner = useMemo(() => {
        for (const [a, b, c] of WINNING_LINES) {
            if (
                matrix[a] &&
                matrix[a] === matrix[b] &&
                matrix[a] === matrix[c]
            ) {
                return matrix[a];
            }
        }
        return null;
    }, [matrix]);

    // Derive turn based on how many moves have been made
    const isXNext = matrix.filter(Boolean).length % 2 === 0;
    const turn = isXNext ? "X" : "O";
    const isDraw = !winner && matrix.every(Boolean);

    const handleReset = () => {
        setMatrix(Array(9).fill(null));
    };

    const handleClick = (i) => {
        if (winner || matrix[i]) return;

        setMatrix((prev) => {
            const next = [...prev];
            next[i] = turn;
            return next;
        });
    };

    return (
        <div>
            <h3 className="tictactoe__winner">
                {winner
                    ? `Winner is: ${winner}`
                    : isDraw
                      ? "It's a Draw!"
                      : `Turn: ${turn}`}
            </h3>
            <div className="tictactoe__container">
                {matrix.map((cell, i) => (
                    <button
                        className="tictactoe__cell"
                        onClick={() => handleClick(i)}
                        type="button"
                        key={i}
                        disabled={!!winner || !!cell}
                        aria-label={`Cell ${i}, ${cell||"empty"}`}
                    >
                        {cell}
                    </button>
                ))}
            </div>
            <button
                type="button"
                className="tictactoe__btn"
                onClick={handleReset}
            >
                Reset
            </button>
        </div>
    );
}
