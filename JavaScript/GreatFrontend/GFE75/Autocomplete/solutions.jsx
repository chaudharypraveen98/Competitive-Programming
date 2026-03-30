import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import "./solutions.css";
import { fetchWithTimeout } from "./helper";

export const AutoComplete = () => {
  const [searchText, setSearchText] = useState("");
  const cache = useRef({});
  const [searchResults, setSearchResults] = useState([]);
  const [selectedTextIndex, setSelectedTextIndex] = useState(null);
  const [shouldSearch, setShouldSearch] = useState(false);
  const [isSelected, setIsSelected] = useState(false);

  const fetchData = async (word) => {
    try {
      const tempResult = await fetchWithTimeout(
        `https://api.datamuse.com/words?sp=${word}`,
      ).then((res) => res.json());
      if (tempResult) {
        return tempResult;
      } else {
        return [];
      }
    } catch (err) {
      console.log("err", err);
      return [];
    }
  };

  const getData = async (characters) => {
    if (characters.length < 3) return; 
    if (cache.current[characters]) {
      console.log("find in cache", cache.current[characters]);
      return cache.current[characters];
    } else {
      const returnedData = await fetchData(characters);
      cache.current = {
        ...cache.current,
        [characters]: returnedData,
      };
      return returnedData;
    }
  };

  const debounce = (func, wait = 500) => {
    let timer;
    return function (...args) {
      clearTimeout(timer);
      timer = setTimeout(() => {
        func.apply(this, args);
      }, wait);
    };
  };

  const handleInputChange = useCallback(
    debounce(async (text) => {
      if (!text) return;
      const results = await getData(text);
      setSearchResults(results);
    }),
    [],
  );

  useEffect(() => {
    setSelectedTextIndex(null);
    if (searchText && shouldSearch) {
      setIsSelected(false);
      handleInputChange(searchText);
    } else {
      setSearchResults([]);
    }
    setShouldSearch(true);
  }, [searchText]);

  const handleKeyDown = (e) => {
    if (e.key === "ArrowUp") {
      e.preventDefault();
      setSelectedTextIndex((prev) =>
        prev === null ? 0 : prev > 0 ? prev - 1 : prev,
      );
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      setSelectedTextIndex((prev) =>
        prev === null ? 0 : prev >= searchResults?.length - 1 ? prev : prev + 1,
      );
    } else if (e.key === "Enter" && selectedTextIndex !== null) {
      handleSelect(searchResults[selectedTextIndex]?.word);
    }
  };

  const handleSelect = (word) => {
    setIsSelected(true);
    setSearchText(word);
    setShouldSearch(false);
    setSearchResults([]);
  };
  console.log("selected index", selectedTextIndex);

  return (
    <div className="main-container">
      <div className="searchInputContainer">
        <label htmlFor="auto-complete">Search Anything !!</label>
        <input
          type="text"
          id="auto-complete"
          placeholder="search anything"
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)}
          role="searchbox"
          aria-autocomplete="list"
          className="inputBox"
          aria-expanded={searchResults?.length > 0}
          aria-controls="result-listbox"
          onKeyDown={handleKeyDown}
        />
      </div>
      {searchResults?.length > 0 ? (
        <div className="resultContainer" id="result-listbox" role="listbox">
          {searchResults.map((result, index) => {
            return (
              <div
                key={result?.word}
                className={`resultItem ${selectedTextIndex === index ? "resultItem--selected" : ""}`}
                role="option"
                aria-selected={selectedTextIndex === index}
                onClick={() => {
                  handleSelect(result?.word);
                }}
              >
                <div className="resultTitle">{result?.word}</div>
              </div>
            );
          })}
        </div>
      ) : searchText && !isSelected ? (
        <div className="resultContainer">
          <h4>No Results Found</h4>
        </div>
      ) : isSelected ? (
        <h4>Content loading...</h4>
      ) : (
        <h5>Write something to start</h5>
      )}
    </div>
  );
};
