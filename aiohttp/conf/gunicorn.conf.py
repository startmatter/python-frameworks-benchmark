workers = 2
bind = "0.0.0.0:8080"
timeout ="300"
worker_class = "aiohttp.GunicornUVLoopWebWorker"
chdir = "/aiohttp/"