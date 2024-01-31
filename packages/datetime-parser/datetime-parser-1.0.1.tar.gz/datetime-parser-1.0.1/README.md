# datetime-parser

datetime can be many different formats and often we want to express a time relative 
to the current time, such as `10 minutes ago`. This module is able to handle all datetime formats
as well as our custom relative time format.

### Relative datetime format:
```
For the current time:
    now
Any other time:
    (+/-)(integer) (milliseconds|seconds|minutes|days|weeks|months|years)
    
examples:
    now
    -1 months
    +3 days
    -123 seconds
```

## Parse Datetime
To parse a datetime (not including relative time), you can use the `try_parse_dt` function. This
will return a pendulum object
```python
from datetime_parser import try_parse_dt

example = "2020-02-02 10:10:10"
example_obj = try_parse_datetime(example)
```

## Parse Relavite Time
To parse a datetime or relative datetime, use `is_datetime`.
```python
from datetime_parser import is_datetime

example = "-5 minutes"
example_obj = is_datetime(example)
```
