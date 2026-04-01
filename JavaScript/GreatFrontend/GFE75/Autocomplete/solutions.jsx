import { useCallback, useEffect, useMemo, useRef, useState } from "react";
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

  return (
    <div className="relative">
      <div className="mb-4">
        <label
          htmlFor="auto-complete"
          className="block text-sm font-medium mb-2 text-slate-200"
        >
          Search Anything !!
        </label>
        <input
          type="text"
          id="auto-complete"
          placeholder="search anything"
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)}
          role="searchbox"
          aria-autocomplete="list"
          className="w-full p-2 rounded border border-slate-700 bg-slate-800 text-slate-100 placeholder:text-slate-500 focus:border-indigo-400 focus:ring-indigo-500 focus:ring-1"
          aria-expanded={searchResults?.length > 0}
          aria-controls="result-listbox"
          onKeyDown={handleKeyDown}
        />
      </div>
      {searchResults?.length > 0 ? (
        <div
          className="absolute top-16 max-h-48 overflow-y-auto rounded w-full bg-slate-900 border border-slate-700 shadow-lg z-10"
          id="result-listbox"
          role="listbox"
        >
          {searchResults.map((result, index) => {
            const isActive = selectedTextIndex === index;
            return (
              <div
                key={result?.word}
                className={`border-b border-slate-700 cursor-pointer p-2 ${isActive ? "bg-slate-700 text-white" : "bg-slate-800 text-slate-200 hover:bg-slate-700"}`}
                role="option"
                aria-selected={isActive}
                onClick={() => {
                  handleSelect(result?.word);
                }}
              >
                <div className="text-sm font-bold text-left">
                  {result?.word}
                </div>
              </div>
            );
          })}
        </div>
      ) : searchText && !isSelected ? (
        <div className="mt-4 p-4 rounded border border-slate-700 bg-slate-900 text-slate-100">
          <h4 className="text-lg font-semibold">No Results Found</h4>
        </div>
      ) : isSelected ? (
        <h4 className="mt-4 text-lg font-semibold text-slate-200">
          Content loaded - Search Successfull
        </h4>
      ) : (
        <h5 className="mt-4 text-sm text-slate-500">
          Write something to start
        </h5>
      )}
    </div>
  );
};
