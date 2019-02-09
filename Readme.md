# Python's Web Framework Benchmarks

## Participants

* **[Django](https://github.com/django/django)** (2.1.4)
* **[Flask](https://github.com/pallets/flask)** (1.0.2)
* **[AioHTTP](https://github.com/aio-libs/aiohttp)** (3.5.1)
* **[Sanic](https://github.com/huge-success/sanic)** (18.12)
* **[Tornado](https://github.com/tornadoweb/tornado)** (5.1.1)

## Start Frameworks and Benchmarks

### Start Framework Server

To run any framework you need:

1. Go to the framework directory. For example: ```cd aiohttp```

2. Start the server using a script: ```bash start.sh```

_To stop the server script is used:_ ```bash stop.sh```

### Start Benchmark

The **[wrk](https://github.com/wg/wrk)** library is used for benchmarking. Benchmarks ran with the following parameters

* Threads = 12 (total number of threads to use)
* Connections = 400 (total number of HTTP connections to keep open with each thread handling N = connections/threads)
* Duration = 30s (duration of the test)

To run the benchmark for current framework you should run the command:

```wrk -t12 -c400 -d30s http://127.0.0.1:8080/db```

## Contributors

* **[Maksim Larkin](https://github.com/maximzah)**
* **[Yauheni Holik](https://github.com/yauheni-holik)**
* **[Vladimir Rubin](https://github.com/VladimirRubin)**