# Algorithm for the file-system crawler.

## Input:
* Takes absolute directory to start the crawl.

## Output:
* Does the operation defined by doOperation function on each file found during
  crawl.

* Discrimination based on file-type  can be included for various file types in
  doOperation function.

## Algo:

> doOperation (currentFile):
>     * based of file type apply discrimination and do the operation.
>
> allThreadsTerminated():
>     * Checks each bit of isDone for the over-all termination status
>
> Crawl (Qindex):
>     * while Qindex is outOfBound and (allThreadsTerminated() == True):
>             * if Qindex outOfBound:
>                     * continue
>             * LOCK
>                     * Iterate from Qindex till you find and index
>                        with value 0.
>                     * Keep updating Qindex.
>             * UNLOCK
>             * currentCrawlDir <= key(Qindex)
>             * Get files/directories in the currentCrawlDir
>             * doOperation on files/subDirs
>             * LOCK
>                     * Enqueue Subdirs in queue of key value pair
>                      * - (where key is absolute subdir path and value 0/1)
>                      * - (0: not crawled , 1: crawled)
>             * UNLOCK
>
> masterCrawl (Q):
>     * init all threads maxThreads from index 0
>             * Crawl (0)
>       
>
> initCrawl (rootCrawlDir, maxThreads = 10):
>     * Initialize a global integer "isDone" to zero.
>      * - where each bit corresponds to its status, whether done or not.
>     * Initialize a Queue with rootCrawlDirectory with value as 0.
>     * masterCrawl (Q)
