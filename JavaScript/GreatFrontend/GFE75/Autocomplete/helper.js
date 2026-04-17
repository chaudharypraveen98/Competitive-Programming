export const fetchWithTimeoutAndRetry = async (
    url,
    options,
    timeout = 5000,
    delay = 3000,
    retries = 3,
) => {
    const abortController = new AbortController();
    const timer = setTimeout(() => abortController.abort(), timeout);

    try {
        const res = await fetch(url, {
            ...options,
            signal: abortController.signal,
        });
        if (
            !res.ok &&
            (res.status >= 500 || res.status === 429) &&
            retries > 0
        ) {
            throw new Error("Server Error");
        }
        return res;
    } catch (error) {
        const isTimeout = error.name === "AbortError";
        if (retries > 0) {
            await new Promise((resolve) => setTimeout(resolve, delay));

            return fetchWithTimeoutAndRetry(
                url,
                options,
                timeout,
                delay * 2,
                retries - 1,
            );
        }
        if (isTimeout) {
            throw new Error("Request timed out after multiple attempts");
        }
        throw error;
    } finally {
        clearTimeout(timer);
    }
};
