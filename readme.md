# Apache Egress Estimate

Compile the "sent bytes" data from Apache logs to estimate the amount of egress from a locally hosted application.

Note that sent bytes does not include HTTP headers so these figures will undercount by that much. Headers are trivial relative to most file sizes but web apps involve _a lot_ of requests with little to no content (think: non-2XX respones, like 302 redirects) where the headers become a factor.

CLI progress bar
https://pypi.org/project/progress/

Parallel processing

https://httpd.apache.org/docs/2.4/logs.html
