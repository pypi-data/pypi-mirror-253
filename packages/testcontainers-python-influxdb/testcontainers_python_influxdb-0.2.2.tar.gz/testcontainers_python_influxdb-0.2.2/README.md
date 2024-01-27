Brings InfluxDB in testcontainers-python (until [PR #413](https://github.com/testcontainers/testcontainers-python/pull/413) is merged).
This project is hosted at https://github.com/Purecontrol/testcontainers-python-influxdb.
Thanks to my employer - [Purecontrol](https://www.purecontrol.com/) - for sponsoring the development of this testing utility 🙏

# Installation in your project

This package supports versions 1.x and 2.x of InfluxDB.
Specify the version you want to use during the installation so that only the needed Python client library will be installed.

- if you use `pip`:

```sh
# for InfluxDB 1.x versions
pip install "testcontainers-python-influxdb[influxdb1]"

# for InfluxDB 2.x versions
pip install "testcontainers-python-influxdb[influxdb2]"

# for both InfluxDB 1.x and 2.x versions (unlikely, but who knows?)
pip install "testcontainers-python-influxdb[influxdb1,influxdb2]"
```

- if you use `poetry`:

```sh
# for InfluxDB 1.x versions
poetry add "testcontainers-python-influxdb[influxdb1]"

# for InfluxDB 2.x versions
poetry add "testcontainers-python-influxdb[influxdb2]"

# for both InfluxDB 1.x and 2.x versions (unlikely, but who knows?)
poetry add "testcontainers-python-influxdb[influxdb1,influxdb2]"
```

# Use cases

## InfluxDB v1

```python
from influxdb.resultset import ResultSet
from testcontainers_python_influxdb.influxdb1 import InfluxDb1Container

def test_create_and_retrieve_datapoints():
    with InfluxDb1Container("influxdb:1.8") as influxdb1_container:
        influxdb1_client = influxdb1_container.get_client()
        databases = influxdb1_client.get_list_database()
        assert len(databases) == 0, "the InfluxDB container starts with no database at all"

        # creates a database and inserts some datapoints
        influxdb1_client.create_database("testcontainers")
        databases = influxdb1_client.get_list_database()
        assert len(databases) == 1, "the InfluxDB container now contains one database"
        assert databases[0] == {"name": "testcontainers"}

        influxdb1_client.write_points(
            [
                {"measurement": "influxdbcontainer", "time": "1978-11-30T09:30:00Z", "fields": {"ratio": 0.42}},
                {"measurement": "influxdbcontainer", "time": "1978-12-25T10:30:00Z", "fields": {"ratio": 0.55}},
            ],
            database="testcontainers",
        )

        # retrieves the inserted datapoints
        datapoints_set: ResultSet = influxdb1_client.query(
            "select ratio from influxdbcontainer;", database="testcontainers"
        )
        datapoints = list(datapoints_set.get_points())
        assert len(datapoints) == 2, "2 datapoints are retrieved"

        datapoint = datapoints[0]
        assert datapoint["time"] == "1978-11-30T09:30:00Z"
        assert datapoint["ratio"] == 0.42

        datapoint = datapoints[1]
        assert datapoint["time"] == "1978-12-25T10:30:00Z"
        assert datapoint["ratio"] == 0.55
```

## InfluxDB v2

```python
from datetime import datetime
from influxdb_client import Bucket
from influxdb_client.client.write_api import SYNCHRONOUS
from testcontainers_python_influxdb.influxdb2 import InfluxDb2Container

def test_create_and_retrieve_datapoints():
    with InfluxDb2Container(
        "influxdb:2.7",
        init_mode="setup",
        username="root",
        password="secret-password",
        org_name="testcontainers-org",
        bucket="my-init-bucket",
        admin_token="secret-token",
    ) as influxdb2_container:
        influxdb2_client, test_org = influxdb2_container.get_client(token="secret-token", org_name="testcontainers-org")
        assert influxdb2_client.ping(), "the client can connect to the InfluxDB instance"

        # ensures that the bucket does not exist yet
        buckets_api = influxdb2_client.buckets_api()
        bucket: Bucket = buckets_api.find_bucket_by_name("testcontainers")
        assert bucket is None, "the test bucket does not exist yet"

        # creates a test bucket and insert a point
        buckets_api.create_bucket(bucket_name="testcontainers", org=test_org)
        bucket: Bucket = buckets_api.find_bucket_by_name("testcontainers")
        assert bucket.name == "testcontainers", "the test bucket now exists"

        write_api = influxdb2_client.write_api(write_options=SYNCHRONOUS)
        write_api.write(
            "testcontainers",
            "testcontainers-org",
            [
                {"measurement": "influxdbcontainer", "time": "1978-11-30T09:30:00Z", "fields": {"ratio": 0.42}},
                {"measurement": "influxdbcontainer", "time": "1978-12-25T10:30:00Z", "fields": {"ratio": 0.55}},
            ],
        )

        # retrieves the inserted datapoints
        query_api = influxdb2_client.query_api()
        tables = query_api.query('from(bucket: "testcontainers") |> range(start: 1978-11-01T22:00:00Z)', org=test_org)
        results = tables.to_values(["_measurement", "_field", "_time", "_value"])

        assert len(results) == 2, "2 datapoints were retrieved"
        assert results[0] == ["influxdbcontainer", "ratio", datetime.fromisoformat("1978-11-30T09:30:00+00:00"), 0.42]
        assert results[1] == ["influxdbcontainer", "ratio", datetime.fromisoformat("1978-12-25T10:30:00+00:00"), 0.55]
```

# Development

## Tests

- install the libraries for 1.x and 2.x clients:

```sh
poetry install --all-extras
```

- run the automated tests:

```sh
# directly with poetry
poetry run pytest -v
```

Code coverage (with [missed branch statements](https://pytest-cov.readthedocs.io/en/latest/config.html?highlight=--cov-branch)):

```sh
poetry run pytest -v --cov=testcontainers_python_influxdb --cov-branch --cov-report term-missing --cov-fail-under 94
```

## Code conventions

The code conventions are described and enforced by [pre-commit hooks](https://pre-commit.com/hooks.html) to maintain style and quality consistency across the code base.
The hooks are declared in the [.pre-commit-config.yaml](.pre-commit-config.yaml) file.

When you contribute, set the git hooks (pre-commit and commit-msg types) on your development environment:

```sh
poetry run pre-commit install --hook-type pre-commit --hook-type commit-msg
```

Before committing, you can check your changes manually with:

```sh
# put all your changes in the git staging area (or add the changes manually and skip this)
git add -A

# run all hooks
poetry run pre-commit run --all-files

# run a specific hook
poetry run pre-commit run ruff --all-files
```

# Licence

Unless stated otherwise, all works are licensed under the [Apache 2.0](https://spdx.org/licenses/Apache-2.0.html), a copy of which is included [here](LICENSE).
