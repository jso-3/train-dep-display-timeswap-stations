import os
import re

# validate platform number
def parsePlatformData(platform):
    if platform is None:
        return ""
    elif bool(re.match(r'^(?:\d{1,2}[A-D]|[A-D]|\d{1,2})$', platform)):
        return platform
    else:
        return ""

def loadConfig():
    data = {
        "journey": {},
        "api": {}
    }

    data["targetFPS"] = int(os.getenv("targetFPS") or 70)
    data["refreshTime"] = int(os.getenv("refreshTime") or 180)
    data["fpsTime"] = int(os.getenv("fpsTime") or 180)
    data["screenRotation"] = int(os.getenv("screenRotation") or 2)
    data["screenBlankHours"] = os.getenv("screenBlankHours") or ""
    data["headless"] = False
    if os.getenv("headless", "").upper() == "TRUE":
        data["headless"] = True

    data["debug"] = False
    if os.getenv("debug", "").upper() == "TRUE":
        data["debug"] = True
    else:
        if os.getenv("debug") and os.getenv("debug").isnumeric():
            data["debug"] = int(os.getenv("debug"))

    data["dualScreen"] = False
    if os.getenv("dualScreen", "").upper() == "TRUE":
        data["dualScreen"] = True
    data["firstDepartureBold"] = True
    if os.getenv("firstDepartureBold", "").upper() == "FALSE":
        data["firstDepartureBold"] = False
    data["hoursPattern"] = re.compile("^((2[0-3]|[0-1]?[0-9])-(2[0-3]|[0-1]?[0-9]))$")

    data["journey"]["departureStation"] = os.getenv("departureStation") or "PAD"

    data["journey"]["destinationStation"] = os.getenv("destinationStation") or ""
    if data["journey"]["destinationStation"] == "null" or data["journey"]["destinationStation"] == "undefined":
        data["journey"]["destinationStation"] = ""

    # --- NEW CODE START ---
    data["journey"]["destinationStation2"] = os.getenv("destinationStation2") or ""
    if data["journey"]["destinationStation2"] == "null" or data["journey"]["destinationStation2"] == "undefined":
        data["journey"]["destinationStation2"] = ""
    # --- NEW CODE END ---

    data["journey"]["individualStationDepartureTime"] = False
    if os.getenv("individualStationDepartureTime", "").upper() == "TRUE":
        data["journey"]["individualStationDepartureTime"] = True

    data["journey"]["outOfHoursName"] = os.getenv("outOfHoursName") or "London Paddington"
    data["journey"]["stationAbbr"] = {"International": "Intl."}
    data["journey"]['timeOffset'] = os.getenv("timeOffset") or "0"
    data["journey"]["screen1Platform"] = parsePlatformData(os.getenv("screen1Platform"))
    data["journey"]["screen2Platform"] = parsePlatformData(os.getenv("screen2Platform"))

    # --- NEW CODE START ---
    # Load the second station configuration
    data["journey"]["departureStation2"] = os.getenv("departureStation2") or ""
    
    # Load the swap time (hour of day, 0-23). Default to None if not set.
    swap_val = os.getenv("stationSwapTime")
    data["journey"]["stationSwapTime"] = int(swap_val) if swap_val and swap_val.isnumeric() else None
    # --- NEW CODE END ---

    data["api"]["apiKey"] = os.getenv("apiKey") or None
    data["api"]["operatingHours"] = os.getenv("operatingHours") or ""

    data["showDepartureNumbers"] = False
    if os.getenv("showDepartureNumbers", "").upper() == "TRUE":
        data["showDepartureNumbers"] = True

    return data
