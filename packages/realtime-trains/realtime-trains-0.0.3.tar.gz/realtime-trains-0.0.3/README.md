# Introduction #

This is an unofficial Python library for the [Realtime Trains API](https://www.realtimetrains.co.uk/).

The library allows you to make calls to the Realtime Trains API, and receive full response as JSON, or as custom objects. Some basic helper filtering of data is also included.

# Requirements #

This library requires you to use your own API key, which (at the time of writing) can be obtained for free from Realtime Trains [developer website](https://api.rtt.io/).

Once registered and logged in, please make note of the **API Auth Credentials** that have automatically been generated for your account.

# Installation #

Use pip to install this library. We recommend you use it within a virtual environment (either with `venv` or `poetry`).

```bash
pip install realtime-trains
```

# Usage #

To be able to use the library, you need to authenticate yourself. The result will be an object which you can then use to query the Realtime Trains data.

```python
from realtime_trains.realtime_trains.api import RealtimeTrainsApi, SearchOptions

rtt = RealtimeTrainsApi(username="<your_rtt_username>", password="<your_rtt_password>")
```

## Request station information ##

To specify the search options, use the `SearchOptions` class.

```python
options = SearchOptions(
	from_station = "CLJ",	# required
	to_station = "WAT",		# optional
	date = "25 Jan 2024", 	# optional
	time = "13:45",			# optional
	platform = "2",			# optional
	num_results = 5,		# optional
	passenger_only = True,	# optional
	show_arrivals = False,	# optional
	show_trains_only = True	# optional
)
```

**NOTE:** Not all options apply to all calls.

After you have created your authenticated object and you specified the search options, you can start requesting data.

### Get raw json response ###

```python
json = rtt.get_search_json(options)
```

### Get resulting data as an object ###

```python
data = rtt.get_search(options)
```

### Get data as a list of train services ###

```python
services = rtt.get_search_services(options)
```

# Reporting issues #

Please report all the issues and feature requests via [GitHub](https://github.com/mbukovac/realtime-trains/issues).

Enjoy!