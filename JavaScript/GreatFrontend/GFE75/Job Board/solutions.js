import { useState, useEffect } from "react";

const JobCard = ({ job }) => {
  return (
    <div className="job-container">
      <div className="job-title">{job.title}</div>
      <div className="job-desc">
        By {job.by} • {new Date(job.time * 1000).toLocaleString()}
      </div>
    </div>
  );
};

export default function App() {
  const [jobIds, setJobIds] = useState([]);
  const [jobs, setJobs] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const loadMoreJobs = () => {
    const nextItems = jobIds?.slice(jobs.length, jobs.length + 6);
    fetchJobs(nextItems);
  };

  const fetchJobs = async (idsToFetch) => {
    setIsLoading(true);
    const allPromises = idsToFetch?.map((jobId) =>
      fetch(`https://hacker-news.firebaseio.com/v0/item/${jobId}.json`).then(
        (res) => res.json(),
      ),
    );
    const tempJobs = await Promise.all(allPromises);
    setJobs((prev) => [...prev, ...tempJobs]);

    setIsLoading(false);
  };
  useEffect(() => {
    let isCancelled = false;

    fetch("https://hacker-news.firebaseio.com/v0/jobstories.json")
      .then((res) => res.json())
      .then((data) => {
        if (!isCancelled) {
          setJobIds(data);
          fetchJobs(data.slice(0, 6));
        }
      })
      .catch((err) => {
        console.error("error", err);
      });

    return () => (isCancelled = true);
  }, []);

  return (
    <div className="main-container">
      <div className="main-title">Hacker News Jobs Board</div>
      <div className="jobs-container">
        {jobs?.map((jobItem) => (
          <JobCard job={jobItem} key={jobItem.id} />
        ))}
      </div>
      {jobIds.length > jobs.length && !isLoading ? (
        <button className="load-more-button" onClick={() => loadMoreJobs()}>
          Load More Jobs
        </button>
      ) : null}
      {isLoading ? <h2>Loading...</h2> : null}
    </div>
  );
}
