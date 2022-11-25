# API benchmarking tool

This is a tool to benchmark the performance of a Rest API. It is written in Python and uses the [Locust](https://locust.io/) framework. It is basically a wrapper around Locust to make it easier to use by creating scenarios based on a configuration file written in YAML.

Each endpoints can be added in the configuration file and the tool will generate the corresponding Locust tasks. It also allows to define a payload file for each endpoint which can be used to pass the parameters to the API.

## Running the benchmark
The wrapper is written in Python and uses the Locust framework. It is recommended to use a virtual environment to install the dependencies.

### Install the dependencies
```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Configuration
The configuration file is written in YAML and kept in `conf/api_conf.yaml` and contains the following sections:

```yaml
apis:
  - name: <NAME FOR THE REQUEST 1>
    path: <URL PATH 1>
    params: <PAYLOAD FILE>
  - name: <NAME FOR THE REQUEST 2>
    path: <URL PATH 2>
    params: <PAYLOAD FILE>
...
```

There is also a `locust.conf` file which contains the configuration for the Locust server. Use `locust --help` to see the available options.

**NOTE**: The payload file should be kept in the `data` directory.
A sample` api_conf.yaml` and `locust.conf` is provided in the `conf` directory as well as a payload file in `data` directory.

### Running the benchmark

Once the configuration is done, run the following command to start the benchmark:

```bash
$ locust --config conf/locust.conf
```

As per the provided `locust.conf` file, the benchmark will be run as headless and a report will be generated in `report.html` in current directory.


### Running the benchmark with docker

```bash
$ docker build -t api-benchmark .
$ docker run -v $(pwd):/app api-benchmark
```

### Running the benchmark with docker-compose

```bash
$ docker compose up
```

Use below command to start a benchmark with a master and 2 workers.

```bash
$ docker compose up --scale worker=2
```

## Assumptions
- The API is a Rest API
- Only supports GET requests
- 404 response is considered as a success
