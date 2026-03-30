export const fetchWithTimeout=async (url, options, timeout=5000)=>{
    const abortController = new AbortController();
    const timer = setTimeout(()=>abortController.abort(), timeout)

    try{
        const res = await fetch(url,{
            ...options,
            signal: abortController.signal
        })
        return res
    } finally {
        clearTimeout(timer)
    }
}   