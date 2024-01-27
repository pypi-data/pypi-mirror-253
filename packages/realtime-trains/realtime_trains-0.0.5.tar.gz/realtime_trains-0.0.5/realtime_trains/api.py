from typing import Optional

import dateutil.parser
import httpx
from pydantic import BaseModel
from .models import Search, Service

class SearchOptions(BaseModel):
	"""Options to pass to the Realtime Trains API."""
	from_station: str
	to_station: Optional[str] = None
	date: Optional[str] = None
	time: Optional[str] = None
	platform: Optional[str] = None
	num_results: Optional[int] = None
	passenger_only: Optional[bool] = True
	show_arrivals: Optional[bool] = False
	show_trains_only: Optional[bool] = True

class RealtimeTrainsApi:
	_BASE_URL: str = "https://api.rtt.io/api/v1/json/"

	def __init__(self, username: str, password: str) -> None:
		"""Constructor.

		Args:
			username (str): Username provided by Railtime Trains.
			password (str): Password provided by Realtime Trains.
		"""
		self.username = username
		self.password = password

	def _fetch(self, url: str) -> None:
		"""Fetch data from the Realtime Trains API.

		Args:
			url (str): URL to fetch data from.

		Raises:
			httpx.HTTPError: Error thrown if the request fails.

		Returns:
			str: json data returned from the Realtime Trains API.
		"""
		response = httpx.get(url, auth=(self.username, self.password))

		if response.status_code == 200:
			return response.json()

		raise httpx.HTTPError(f"Request failed with status code {response.status_code}")

	def _fetch_search_data(self, params: SearchOptions) -> dict:
		"""Fetch data from the Realtime Trains API.

		Args:
			params (SearchOptions): Object containing the options to pass to the Realtime Trains API.

		Returns:
			dict: Raw json data returned from the Realtime Trains API.
		"""
		access_point = self._BASE_URL + "search/" + params.from_station

		# If we have a to_station, add it to the access point
		if params.to_station is not None:
			access_point += "/to/" + params.to_station

		# If we have a date, add it to the access point
		if params.date is not None:
			formattedDate = dateutil.parser.parse(params.date).strftime("%Y-%m-%d")
			year, month, day = formattedDate.split("-")
			access_point += f"/{year}/{month}/{day}"

		# If we have a time, add it to the access point
		if params.time is not None:
			formattedTime = dateutil.parser.parse(params.time).strftime("%H%M")
			access_point += f"/{formattedTime}"

		# If we want to show arrivals, add it to the access point
		if params.show_arrivals:
			access_point += "/arrivals"

		print (access_point)
		return self._fetch(access_point)

	def get_search_json(self, params: SearchOptions) -> dict:
		"""Get raw json data from the Realtime Trains API. Data will be pulled from API automatically.

		Args:
			params (SearchOptions): Object containing the options to pass to the Realtime Trains API.

		Returns:
			dict: Raw json data returned from the Realtime Trains API.
		"""
		return self._fetch_search_data(params)

	def get_search(self, params: SearchOptions) -> Search:
		"""Get data as a Search object. Data will be pulled from API automatically.

		Args:
			params (SearchOptions): Object containing the options to pass to the Realtime Trains API.

		Returns:
			Search: Object containing the data returned from the Realtime Trains API.
		"""
		try:
			json = self.get_search_json(params)

		except Exception as e:
			print(e)

		""" Convert json to a Search object """
		return Search(**json)

	def get_search_services(self, params: SearchOptions) -> list[Service]:
		"""Get a list of services. Data will be pulled from API automatically.

		Args:
			params (SearchOptions): Object containing the options to pass to the Realtime Trains API.

		Returns:
			list[Service]: List of services returned from the Realtime Trains API.
		"""
		services = []

		try:
			search_data = self.get_search(params)

			# Get the list of services from the search data
			services = search_data.services

			# Loop through the list of services and remove any that are not on the desired platform
			if params.platform is not None:
				services = [service for service in services if service.locationDetail.platform == params.platform]

			# Loop through the list and remove any services that are not passenger services
			if params.passenger_only:
				services = [service for service in services if service.isPassenger]

			if params.show_trains_only:
				services = [service for service in services if service.serviceType == "train"]

			# If we specified the number of results to return, only return that number of results
			if params.num_results is not None:
				services = services[:params.num_results]

		except Exception as e:
			print(e)

		return services