# nice_logging

Simple logging library that has colored and timestamped output by default. Can be used as a drop-in replacement.

## Installation

```pip install nice_logging```

(Or just grab the .py file)

## Usage

```python
import nice_logging
nice_logging.basicConfig(level=nice_logging.DEBUG)
logger = nice_logging.getLogger(__name__)
logger.info("Hello")
```
```
2023-07-23 11:27:33,571 [INFO ] [__main__] Hello
```

Or:

```python
import nice_logging as logging
```

## Structured Logging

nice_logging has support for rudimentary structured logging. If you use `getStructuredLogger` instead of `getLogger` (or instantiate a `StructuredLogger`), you will get a logger whose log functions take a single message, and any number of keyword arguments, which are aggregated in a single dict. The resulting `LogRecord` will have the attribute `structured` set to `True`, and `structured_data` to the dict.
