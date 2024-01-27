from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel, validator

class Location(BaseModel):
	name: str
	crs: str
	country: str
	system: str

class OriginDestination(BaseModel):
	@validator("workingTime", pre=True)
	def parse_workingTime(cls, value):
		return datetime.strptime(value, "%H%M%S") if value else None

	@validator("publicTime", pre=True)
	def parse_publicTime(cls, value):
		return datetime.strptime(value, "%H%M") if value else None

	tiploc: str
	description: str
	workingTime: Optional[datetime] = None
	publicTime: Optional[datetime] = None

class LocationDetail(BaseModel):
	@validator("gbttBookedArrival", "gbttBookedDeparture", "realtimeArrival", "realtimeDeparture", pre=True)
	def parse_time(cls, value):
		return datetime.strptime(value, "%H%M") if value else None

	realtimeActivated: Optional[bool] = None
	tiploc: str
	crs: str
	description: str
	gbttBookedArrival: Optional[datetime] = None
	gbttBookedDeparture: Optional[datetime] = None
	origin: list[OriginDestination]
	destination: list[OriginDestination]
	isCall: Optional[bool] = None
	isPublicCall: Optional[bool] = None
	realtimeArrival: Optional[datetime] = None
	realtimeArrivalActual: Optional[bool] = None
	realtimeArrivalNoReport: Optional[bool] = None
	realtimeDeparture: Optional[datetime] = None
	realtimeDepartureActual: Optional[bool] = None
	realtimeDepartureNoReport: Optional[bool] = None
	platform: Optional[str] = None
	platformConfirmed: Optional[bool] = None
	platformChanged: Optional[bool] = None
	cancelReasonCode: Optional[str] = None
	cancelReasonShortText: Optional[str] = None
	cancelReasonLongText: Optional[str] = None
	displayAs: Optional[str] = None
	serviceLocation: Optional[str] = None
	#wttBookedArrivalDetailed: Optional[str] = None
	#wttBookedDepartureDetailed: Optional[str] = None
	#wttBookedPassDetailed: Optional[str] = None
	#realtimeWttArrivalLatenessDetailed: Optional[str] = None
	#realtimeGbttArrivalLateness: Optional[str] = None
	#realtimeWttDepartureLatenessDetailed: Optional[str] = None
	#realtimeGbttDepartureLateness: Optional[str] = None
	#realtimePassDetailed: Optional[str] = None
	#realtimePassActualDetailed: Optional[str] = None
	#realtimePassNoReportDetailed: Optional[bool] = None
	#lineDetailed: Optional[str] = None
	#lineConfirmedDetailed: Optional[bool] = None
	#pathDetailed: Optional[str] = None
	#pathConfirmedDetailed: Optional[bool] = None

class Service(BaseModel):
	locationDetail: LocationDetail
	serviceUid: str
	runDate: date
	trainIdentity: str
	runningIdentity: Optional[str] = None
	atocCode: str
	atocName: str
	serviceType: str
	isPassenger: bool
	plannedCancel: Optional[bool] = None
	origin: Optional[list[OriginDestination]] = None
	destination: Optional[list[OriginDestination]] = None
	countdownMinutes: Optional[str] = None

class Search(BaseModel):
	location: Location
	services: list[Service]

