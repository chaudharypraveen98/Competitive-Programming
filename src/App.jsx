import { useEffect } from "react";
import { AutoComplete } from "./../JavaScript/GreatFrontend/GFE75/Autocomplete/solutions";
import TrafficLight from "../JavaScript/GreatFrontend/GFE75/Traffic Light/solutions";
import { applyDarkTheme } from "./theme";
import ProgressBar from "../JavaScript/GreatFrontend/GFE75/Progress Bars/ProgressBar";
import Star from "../JavaScript/GreatFrontend/GFE75/StarRating";
import StarRating from "../JavaScript/GreatFrontend/GFE75/StarRating";
import LikeButton from "../JavaScript/GreatFrontend/GFE75/LikeButton";
import Modal from "../JavaScript/GreatFrontend/GFE75/ModalDialog";
import DataTable from "../JavaScript/GreatFrontend/GFE75/DataTable";
import Checkboxes from "../JavaScript/GreatFrontend/GFE75/NestedCheckboxes";
import Stopwatch from "../JavaScript/GreatFrontend/GFE75/Stopwatch";
import DigitalClock from "../JavaScript/GreatFrontend/GFE75/DigitalClock";
import FileExplorer from "../JavaScript/GreatFrontend/GFE75/FileExplorer";
import TransferList from "../JavaScript/GreatFrontend/GFE75/TransferList";

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
                      <h2 className="mb-3 text-xl font-semibold">
                          Transfer List
                      </h2>
                      <TransferList />
                  </div>
                  <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
                      <h2 className="mb-3 text-xl font-semibold">
                          File Explorer
                      </h2>
                      <FileExplorer />
                  </div>
                  <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
                      <h2 className="mb-3 text-xl font-semibold">
                          Digital Clock
                      </h2>
                      <DigitalClock />
                  </div>
                  <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
                      <h2 className="mb-3 text-xl font-semibold">Stop Watch</h2>
                      <Stopwatch />
                  </div>
                  <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
                      <h2 className="mb-3 text-xl font-semibold">Checkboxex</h2>
                      <Checkboxes />
                  </div>
                  <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
                      <h2 className="mb-3 text-xl font-semibold">
                          Autocomplete Demo
                      </h2>
                      <AutoComplete />
                  </div>
                  {/* 
                  <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
                      <h2 className="mb-3 text-xl font-semibold">
                          Traffic Light Demo
                      </h2>
                      <TrafficLight />
                  </div> */}

                  <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
                      <h2 className="mb-3 text-xl font-semibold">
                          Traffic Light Demo
                      </h2>
                      <ProgressBar />
                  </div>

                  <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
                      <h2 className="mb-3 text-xl font-semibold">Star Demo</h2>
                      <StarRating />
                  </div>
                  <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
                      <h2 className="mb-3 text-xl font-semibold">
                          Like Button
                      </h2>
                      <LikeButton />
                  </div>
                  <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
                      <h2 className="mb-3 text-xl font-semibold">Modal</h2>
                      <Modal />
                  </div>
                  <div className="rounded-xl border border-slate-700 bg-slate-900 p-4">
                      <h2 className="mb-3 text-xl font-semibold">Data Table</h2>
                      <DataTable />
                  </div>
              </section>
          </main>
      </div>
  );
}

export default App;
