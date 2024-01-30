# logprof - Simple logging profiler

Python module for simple logging with function timing and memory usuage.


## Installation

```bash
pip install logprof
```

## Usage

Below is an example usage (the performance of the example strategy won't be good).

```python
    import logging
    from logprof import logprof

    logging.basicConfig(level="INFO")

    @logprof("bar")
    def function():
        print("The bit in the middle")

    function()

    class Foo:
        @logprof("class func")
        def bar(self, x=1):
            print(f"bar got x = {x}")

    Foo().bar()

    with logprof("foo"):
        from time import sleep

        sleep(1)
        x = [1] * 2**25  ## 256MB?
        x.append(1000)
        print("The bit in the middle")
```

## Development

Before commit run following format commands in project folder:

```bash
poetry run black .
poetry run isort . --profile black
```
