# Apache Egress Estimate

Compile the "sent bytes" data from Apache logs to estimate the amount of egress from a locally hosted application.

Note that sent bytes does not include HTTP headers so these figures will undercount by at least that much. Headers are trivial relative to most file sizes but web apps involve _a lot_ of requests with little to no content (think: non-2XX responses, like 302 redirects) where the headers become a factor.

## Usage

Requires `pipenv` and a modern python. Download apache logs into the data dir. You will probably need to `tar czf` the logs and do some permissions changes. Look for the `LogFormat` directive in Apache configuration and make sure the `LogParser` call at the top of the script matches it so we know where to pull the date and bytes sent figures from. The script accepts any number of logs as positional arguments.

```sh
# setup project & run
pipenv install
pipenv run ./egress.py data/*
```

## Notes

CLI progress bar
https://pypi.org/project/progress/

Parallel processing
https://docs.python.org/3/library/multiprocessing.html

See sections on Manager and Pool.

Apace `LogFormat` directive:
https://httpd.apache.org/docs/2.4/logs.html

## LICENSE

[ECL Version 2.0](https://opensource.org/licenses/ECL-2.0)
