import { useEffect } from "react";
import { AutoComplete } from "./../JavaScript/GreatFrontend/GFE75/Autocomplete/solutions";
import TrafficLight from "../JavaScript/GreatFrontend/GFE75/Traffic Light/solutions";
import { applyDarkTheme } from "./theme";

function App() {
  useEffect(() => {
    applyDarkTheme();
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100">
      <main className="mx-auto max-w-6xl px-4 py-8">
        <header className="mb-8 flex flex-wrap items-center justify-between gap-4 rounded-xl border border-slate-700 bg-slate-900 p-4">
          <h1 className="text-3xl font-bold">
            Competitive Programming Visualizer
          </h1>
        </header>

        <section className="grid gap-6">
          <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
            <h2 className="mb-3 text-xl font-semibold">Autocomplete Demo</h2>
            <AutoComplete />
          </div>

          <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
            <h2 className="mb-3 text-xl font-semibold">Traffic Light Demo</h2>
            <TrafficLight />
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
