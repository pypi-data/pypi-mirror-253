"""The downloader part of the threedi_scenario_downloader supplies the user
with often used functionality to look up and export 3Di results using the
Lizard API"""
import csv
import logging
import math
import os
from datetime import datetime, timedelta
from time import sleep
from urllib.error import HTTPError
from urllib.parse import urlparse

import requests

LIZARD_URL = "https://demo.lizard.net/api/v4/"
RESULT_LIMIT = 10

_AUTH = {}  # Used to store the api_key globally. Use set/get_api_key.


SCENARIO_FILTERS = {
    "name": "name",
    "name__icontains": "name__icontains",
    "uuid": "uuid",
    "id": "id",
    "model_revision": "model_revision",
    "model_name": "model_name__icontains",
    "organisation": "organisation__icontains",
    "organisation__unique_id": "organisation__unique_id",
    "username": "username__icontains",
    "offset": "offset",
}

# results endpoint
WATER_DEPTH = "depth-dtri"
MAX_WATER_DEPTH = "depth-max-dtri"
WATER_LEVEL = "s1-dtri"
RATE_OF_RISE = "rise-velocity-quad"
PRECIPITATION = "rain-quad"

# basic sub-endpoint
MAX_FLOW_VELOCITY = "ucr-max-quad"
MAX_WATER_LEVEL = "s1-max-dtri"

# arrival sub-endpoint
ARRIVAL_TIME = "depth-first-dtri"

# damage sub-endpoint
TOTAL_DAMAGE = "total-damage"


logger = logging.getLogger(__name__)


def set_api_key(api_key: str):
    _AUTH["api_key"] = api_key


def get_api_key() -> str:
    if not _AUTH.get("api_key"):
        raise RuntimeError("api key hasn't been set with set_api_key()")
    return _AUTH["api_key"]


def print_negative_response(response):
    if response.status_code > 299:
        print("Response content:", response.text)


def find_scenarios(limit=RESULT_LIMIT, **kwargs):
    """return json containing scenarios based on supplied filters"""
    url = f"{LIZARD_URL}scenarios/"

    payload = {"limit": limit}
    for key, value in kwargs.items():
        api_filter = SCENARIO_FILTERS[key]
        payload[api_filter] = value

    r = requests.get(url=url, auth=("__key__", get_api_key()), params=payload)
    r.raise_for_status()
    return r.json()["results"]


def find_scenarios_by_model_slug(model_uuid, limit=RESULT_LIMIT):
    """return json containing scenarios based on model slug"""

    url = f"{LIZARD_URL}scenarios/"
    payload = {"model_name__icontains": model_uuid, "limit": limit}
    r = requests.get(url=url, auth=("__key__", get_api_key()), params=payload)
    r.raise_for_status()
    return r.json()["results"]


def find_scenarios_by_name(name, limit=RESULT_LIMIT):
    """return json containing scenarios based on name"""
    url = f"{LIZARD_URL}scenarios/"
    payload = {"name__icontains": name, "limit": limit}
    r = requests.get(url=url, auth=("__key__", get_api_key()), params=payload)
    r.raise_for_status()
    return r.json()["results"]


def find_scenarios_by_exact_name(name, limit=RESULT_LIMIT):
    """return json containing scenarios based on exact name"""
    url = f"{LIZARD_URL}scenarios/"
    payload = {"name": name, "limit": limit}
    r = requests.get(url=url, auth=("__key__", get_api_key()), params=payload)
    r.raise_for_status()
    return r.json()["results"]


def get_scenario_instance(scenario_uuid):
    """return scenario instance containing all projection and resolution
    information"""
    r = requests.get(
        url=f"{LIZARD_URL}scenarios/{scenario_uuid}/",
        auth=("__key__", get_api_key()),
    )
    r.raise_for_status()
    scenario_instance = r.json()
    return scenario_instance


def get_scenario_instance_results(scenario_uuid, subendpoint=None):
    """get the scenario instance results, either from basic raster results, or
    specific results by using a subendpoint (damage and arrival time)"""
    get_scenario_instance(scenario_uuid)

    if subendpoint:
        url = f"{LIZARD_URL}scenarios/{scenario_uuid}/results/{subendpoint}"
    else:
        url = f"{LIZARD_URL}scenarios/{scenario_uuid}/results"

    r = requests.get(url=url, auth=("__key__", get_api_key()))
    r.raise_for_status()

    if not r.json()["results"]:
        logger.debug(
            """The result data you request is non-existent, or your user
            account does not have the rights to request this data"""
        )
        raise ValueError(
            """The result data you request is non-existent, or your user
            account does not have the rights to request this data"""
        )

    return r.json()["results"]


def get_netcdf_link(scenario_uuid):
    """return url to raw 3Di results"""
    result_list = get_scenario_instance_results(scenario_uuid)

    for result in result_list:
        if result["code"] == "results-3di":
            url = result["attachment_url"]
            return url


def get_aggregation_netcdf_link(scenario_uuid):
    """return url to raw 3Di results"""
    result_list = get_scenario_instance_results(scenario_uuid)

    for result in result_list:
        if result["code"] == "aggregate-results-3di":
            url = result["attachment_url"]

            return url


def get_gridadmin_link(scenario_uuid):
    """return url to gridadministration"""
    result_list = get_scenario_instance_results(scenario_uuid)

    for result in result_list:
        if result["code"] == "grid-admin":
            url = result["attachment_url"]
            return url


def get_logging_link(scenario_uuid):
    result_list = get_scenario_instance_results(scenario_uuid)

    for result in result_list:
        if result["code"] == "logfiles":
            url = result["attachment_url"]
            return url


def get_raster_url(scenario_uuid, raster_code, subendpoint=None) -> str:
    result_list = get_scenario_instance_results(
        scenario_uuid=scenario_uuid, subendpoint=subendpoint
    )

    for result in result_list:
        if result["code"] == raster_code:
            raster_url = result["raster"]
            return raster_url
    # Nothing found, raise an exception to be nice and explicit.
    raise ValueError(f"Raster url for raster_code {raster_code} not found")


def get_raster(scenario_uuid, raster_code, subendpoint=None) -> dict:
    """return json of raster based on scenario uuid and raster type"""

    raster_url = get_raster_url(
        scenario_uuid=scenario_uuid, raster_code=raster_code, subendpoint=subendpoint
    )

    r = requests.get(
        url=raster_url,
        auth=("__key__", get_api_key()),
    )
    r.raise_for_status()

    raster = r.json()
    return raster


def create_raster_task(
    raster, scenario_instance, projection=None, resolution=None, bbox=None, time=None
):
    """create Lizard raster task"""

    x1 = scenario_instance["origin_x"]
    y1 = scenario_instance["origin_y"]
    x2 = scenario_instance["upper_bound_x"]
    y2 = scenario_instance["upper_bound_y"]

    # Take bbox dimensions if not bigger than the scenario extent.
    if bbox:
        # Check for bounding dictionary
        if isinstance(bbox, dict):
            xx1 = bbox["west"]
            yy1 = bbox["south"]
            xx2 = bbox["east"]
            yy2 = bbox["north"]
        else:
            xx1, yy1, xx2, yy2 = (float(i) for i in bbox.split(","))
        if abs(xx2 - xx1) > abs(x2 - x1):
            raise ValueError("Chosen bbox wider than scenario extend")
        if abs(yy2 - yy1) > abs(y2 - y1):
            raise ValueError("Chosen bbox taller than scenario extend")
        x1 = xx1
        y1 = yy1
        x2 = xx2
        y2 = yy2

    if projection is None:
        projection = raster["projection"]

    if resolution is None:
        pixelsize_x = abs(scenario_instance["pixelsize_x"])
        pixelsize_y = abs(scenario_instance["pixelsize_y"])
    else:
        pixelsize_x = resolution
        pixelsize_y = resolution

    width = abs((x2 - x1) / pixelsize_x)
    height = abs((y2 - y1) / pixelsize_y)

    # Check if pixelsize fits the extent, if not, to maintain pixelsize,
    # enlarge the extent
    if not width.is_integer():
        width = math.ceil(width)
        x2 = (width * pixelsize_x) + x1
    if not height.is_integer():
        height = math.ceil(height)
        y2 = (height * pixelsize_y) + y1

    bbox = f"{x1},{y1},{x2},{y2}"

    url = "{}rasters/{}/data/".format(LIZARD_URL, raster["uuid"])

    # non temporal raster
    payload = {
        "width": width,
        "height": height,
        "bbox": bbox,
        "projection": projection,
        "format": "geotiff",
        "async": "true",
    }

    if time is not None:
        # temporal rasters
        check_temporal_request(scenario_instance, time)
        payload["start"] = time

    r = requests.get(url=url, auth=("__key__", get_api_key()), params=payload)
    print_negative_response(r)

    r.raise_for_status()
    return r.json()


# From here untested methods are added
def get_task_status(task_uuid) -> str:
    """return status of task"""
    url = f"{LIZARD_URL}tasks/{task_uuid}/"
    try:
        r = requests.get(url=url, auth=("__key__", get_api_key()))
        r.raise_for_status()
        return r.json()["status"]
    except requests.exceptions.RequestException:
        logger.exception(f"Error while requesting task status for task {task_uuid}")
        return "UNKNOWN"


def get_task_download_url(task_uuid):
    """return url of successful task"""
    if get_task_status(task_uuid) == "SUCCESS":
        url = f"{LIZARD_URL}tasks/{task_uuid}/"
        r = requests.get(url=url, auth=("__key__", get_api_key()))
        r.raise_for_status()
        return r.json()["result"]
    # What to do if task is not a success?


def download_file(url, path):
    """download url to specified path"""
    logger.debug(f"Start downloading file: {url}")
    if "amazon" not in url:
        r = requests.get(url, auth=("__key__", get_api_key()), stream=True)
    else:
        # Amazon s3 request: don't send lizard's auth headers.
        r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(path, "wb") as file:
        for chunk in r.iter_content(1024 * 1024 * 10):
            file.write(chunk)


def download_task(task_uuid, pathname=None):
    """download result of successful task"""
    if get_task_status(task_uuid) == "SUCCESS":
        download_url = get_task_download_url(task_uuid)
        if pathname is None:
            logger.debug(f"download_url: {download_url}")
            logger.debug(f"urlparse(download_url): {urlparse(download_url)}")
            pathname = os.path.basename(urlparse(download_url).path)
            logger.debug(pathname)
        download_file(download_url, pathname)


def download_raster(
    scenario,
    raster_code=None,
    projection=None,
    resolution=None,
    bbox=None,
    time=None,
    pathname=None,
    is_threedi_scenario=True,  # Set to False when requesting rasters that are not a Threedi result.
    export_task_csv=None,
):
    """
    Download raster.
    To download multiple rasters at the same time, simply pass the required
    input parameters as list.
    Scenario and pathname should be of same length. Other parameters can be
    tuple to apply the same settings to all rasters.
    Time format is '%Y-%m-%dT%H:%M:%SZ'.
    """

    # If task is called for single raster, prepare list.
    def transform_to_list(var, length=1) -> list:
        """Transform input to list if for instance only one input is given"""
        if isinstance(var, list):
            return var
        else:
            if isinstance(var, tuple):
                return list(var) * length
            else:  # type(var) in (str, dict, int, type(None), bool, float):
                return [var] * length

    # Transform input parameters to list
    scenario_list = transform_to_list(var=scenario)
    raster_code_list = transform_to_list(var=raster_code, length=len(scenario_list))
    projection_list = transform_to_list(var=projection, length=len(scenario_list))
    resolution_list = transform_to_list(var=resolution, length=len(scenario_list))
    bbox_list = transform_to_list(var=bbox, length=len(scenario_list))
    time_list = transform_to_list(var=time, length=len(scenario_list))
    pathname_list = transform_to_list(var=pathname)
    is_threedi_scenario_list = transform_to_list(
        var=is_threedi_scenario, length=len(scenario_list)
    )

    # Helper parameters.
    processed_list = transform_to_list(var=False, length=len(scenario_list))
    task_id_list = transform_to_list(var=None, length=len(scenario_list))
    task_url_list = transform_to_list(var=None, length=len(scenario_list))

    # Helper for subendpoints
    subendpoint_per_raster_code = {
        ARRIVAL_TIME: "arrival",
        TOTAL_DAMAGE: "damage",
        MAX_FLOW_VELOCITY: "basic",
        MAX_WATER_LEVEL: "basic",
    }

    # Wrong input error
    if len(scenario_list) != len(pathname_list):
        logger.debug("Scenarios and output should be of same length")
        raise ValueError("scenario_list and pathname_list are of different length")

    tasks = []
    # Create tasks
    for (
        (index, scenario),
        raster_code,
        projection,
        bbox,
        resolution,
        time,
        is_threedi_scenario,
    ) in zip(
        enumerate(scenario_list),
        raster_code_list,
        projection_list,
        bbox_list,
        resolution_list,
        time_list,
        is_threedi_scenario_list,
    ):
        if is_threedi_scenario:
            if isinstance(scenario, str):
                # assume 'scenario' is an uuid
                scenario_instance = get_scenario_instance(scenario)
                subendpoint = subendpoint_per_raster_code.get(raster_code)

                raster = get_raster(scenario, raster_code, subendpoint=subendpoint)

            elif isinstance(scenario, dict):
                # assume 'scenario' is a json object
                scenario_instance = scenario

                subendpoint = subendpoint_per_raster_code.get(raster_code)
                # TODO: subendpoint isn't used in get_raster_from_json()
                raster = get_raster_from_json(
                    scenario, raster_code, subendpoint=subendpoint
                )
            else:
                logger.debug(
                    """Invalid scenario: supply a json object
                              or uuid string"""
                )
                raise ValueError(
                    "Invalid scenario: supply a json object or uuid string"
                )
        else:
            # If no bbox are passed the function will probably crash.
            if isinstance(scenario, str) and (bbox is not None):
                raster = {}
                scenario_instance = {}
                raster["uuid"] = scenario
            else:
                raise ValueError(
                    f"Invalid scenario: supply a scenario and bounding box. Scenario: {scenario}"
                )
        # Send task to lizard
        logger.debug("Creating task with the following parameters:")
        logger.debug(f"raster: {raster}")
        logger.debug(f"projection: {projection}")
        logger.debug(f"resolution: {resolution}")
        logger.debug(f"scenario_instance: {scenario_instance}")
        logger.debug(f"bbox: {bbox}")
        logger.debug(f"time: {time}")
        task = create_raster_task(
            raster,
            scenario_instance,
            projection=projection,
            resolution=resolution,
            bbox=bbox,
            time=time,
        )
        task_id_list[index] = task["task_id"]
        task_url_list[index] = task["url"]
        tasks.append(task)

    if export_task_csv is not None:
        logger.debug("Exporting tasks to csv")

        task_export = []

        # Create a list with task url's and pathnames
        for (index, task_id), task_url, pathname in zip(
            enumerate(task_id_list), task_url_list, pathname_list
        ):
            task_export.append({"uuid": task_id, "url": task_url, "pathname": pathname})

        logger.debug(f"task_export: {task_export}")
        with open(export_task_csv, "w", newline="") as f:
            # using csv.writer method from CSV package
            field_names = ["uuid", "url", "pathname"]
            writer = csv.DictWriter(
                f, field_names, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL
            )
            writer.writeheader()
            writer.writerows(task_export)

    # Check status of task and download
    while not all(processed_list):
        for (index, task_uuid), pathname, processed in zip(
            enumerate(task_id_list), pathname_list, processed_list
        ):
            if not processed:
                task_status = get_task_status(task_uuid)

                if task_status == "SUCCESS":
                    # task is a succes, return download url
                    try:
                        logger.debug(
                            f"""Task succeeded, start
                            downloading url: {get_task_download_url(task_uuid)}"""
                        )
                        logger.debug(
                            f"Remaining tasks: {processed_list.count(False) - 1}"
                        )
                        download_task(task_uuid, pathname)
                        processed_list[index] = True

                    except HTTPError as err:
                        if err.code == 503:
                            logger.debug(
                                """503 Server Error: Lizard has lost it.
                                Let's ignore this."""
                            )
                            task_status = "UNKNOWN"
                        else:
                            raise

                elif task_status in ("PENDING", "UNKNOWN", "STARTED", "RETRY"):
                    pass
                else:
                    logger.debug(f"Task {task_uuid} failed, status was: {task_status}")
                    processed_list[index] = True
        sleep(5)


def download_maximum_waterdepth_raster(
    scenario_uuid, projection=None, resolution=None, bbox=None, pathname=None
):
    """download Maximum waterdepth raster"""
    download_raster(
        scenario_uuid,
        MAX_WATER_DEPTH,
        projection=projection,
        resolution=resolution,
        bbox=bbox,
        pathname=pathname,
    )


def download_maximum_waterlevel_raster(
    scenario_uuid, projection=None, resolution=None, bbox=None, pathname=None
):
    """download Maximum waterlevel raster"""
    download_raster(
        scenario_uuid,
        MAX_WATER_LEVEL,
        projection=projection,
        resolution=resolution,
        bbox=bbox,
        pathname=pathname,
    )


def download_maximum_flow_velocity_raster(
    scenario_uuid, projection=None, resolution=None, bbox=None, pathname=None
):
    """download Maximum waterdepth raster"""
    download_raster(
        scenario_uuid,
        MAX_FLOW_VELOCITY,
        projection=projection,
        resolution=resolution,
        bbox=bbox,
        pathname=pathname,
    )


def download_total_damage_raster(
    scenario_uuid, projection=None, resolution=None, bbox=None, pathname=None
):
    """download Total Damage raster"""
    download_raster(
        scenario_uuid,
        TOTAL_DAMAGE,
        projection=projection,
        resolution=resolution,
        bbox=bbox,
        pathname=pathname,
    )


def download_arrival_time_raster(
    scenario_uuid, projection=None, resolution=None, bbox=None, pathname=None
):
    """download arrival time raster"""
    download_raster(
        scenario_uuid,
        ARRIVAL_TIME,
        projection=projection,
        resolution=resolution,
        bbox=bbox,
        pathname=pathname,
    )


def download_waterdepth_raster(
    scenario_uuid,
    projection=None,
    resolution=None,
    time=None,
    bbox=None,
    pathname=None,
):
    """download snapshot of Waterdepth raster,
    time format is '%Y-%m-%dT%H:%M:%SZ'."""
    download_raster(
        scenario_uuid,
        WATER_DEPTH,
        projection=projection,
        resolution=resolution,
        bbox=bbox,
        time=time,
        pathname=pathname,
    )


def download_waterlevel_raster(
    scenario_uuid,
    projection=None,
    resolution=None,
    time=None,
    bbox=None,
    pathname=None,
):
    """download snapshot of Waterlevel raster,
    time format is '%Y-%m-%dT%H:%M:%SZ'."""
    download_raster(
        scenario_uuid,
        WATER_LEVEL,
        projection=projection,
        resolution=resolution,
        bbox=bbox,
        time=time,
        pathname=pathname,
    )


def download_precipitation_raster(
    scenario_uuid,
    projection=None,
    resolution=None,
    time=None,
    bbox=None,
    pathname=None,
):
    """download snapshot of precipitation raster,
    time format is '%Y-%m-%dT%H:%M:%SZ'."""
    download_raster(
        scenario_uuid,
        PRECIPITATION,
        projection=projection,
        resolution=resolution,
        bbox=bbox,
        time=time,
        pathname=pathname,
    )


def download_raw_results(scenario_uuid, pathname=None):
    """downloads the 3Di NetCDF file of the supplied scenario"""
    url = get_netcdf_link(scenario_uuid)
    logger.debug(f"Start downloading raw results: {url}")
    download_file(url, pathname)


def download_aggregated_results(scenario_uuid, pathname=None):
    """downloads the 3Di aggregated NetCDF file of the supplied scenario"""
    url = get_aggregation_netcdf_link(scenario_uuid)
    logger.debug(f"Start downloading aggregated results: {url}")
    download_file(url, pathname)


def download_logging_results(scenario_uuid, pathname=None):
    """downloads the 3Di logging of the supplied scenario"""
    url = get_logging_link(scenario_uuid)
    logger.debug(f"Start downloading logging results: {url}")
    download_file(url, pathname)


def download_grid_administration(scenario_uuid, pathname=None):
    """downloads the 3Di grid administration (.h5 file) of
    the supplied scenario"""
    url = get_gridadmin_link(scenario_uuid)
    logger.debug(f"Start downloading grid administration: {url}")
    download_file(url, pathname)


def get_attachment_links(scenario_json):
    """get links to static scenario results"""
    attachment_links = {}
    scenario_uuid = scenario_json["uuid"]
    result_list = get_scenario_instance_results(scenario_uuid)
    for result in result_list:
        if result["attachment_url"]:
            result_name = result["name"]
            attachment_links[result_name] = result["attachment_url"]
    if attachment_links:
        return attachment_links
    else:
        return None


def rasters_in_scenario(scenario_json, subendpoint=None):
    """return two lists of static and temporal rasters
    including 3di result name and code"""
    scenario_uuid = scenario_json["uuid"]
    result_list = get_scenario_instance_results(
        scenario_uuid=scenario_uuid, subendpoint=subendpoint
    )

    temporal_rasters = []
    static_rasters = []
    for result in result_list:
        if result["raster"]:
            raster_url = result["raster"]
            raster_instance = get_raster(scenario_uuid, result["code"])
            name_3di = result["name"]
            code_3di = result["code"]
            raster_instance["name_3di"] = name_3di
            raster_instance["code_3di"] = code_3di
            if raster_instance["temporal"]:
                temporal_rasters.append(raster_url)
            else:
                static_rasters.append(raster_url)
    return static_rasters, temporal_rasters


def get_raster_download_link(
    raster, scenario_instance, resolution=None, projection=None, bbox=None, time=None
):
    """get url to download raster, time format is '%Y-%m-%dT%H:%M:%SZ'."""
    task = create_raster_task(
        raster=raster,
        scenario_instance=scenario_instance,
        resolution=resolution,
        projection=projection,
        bbox=bbox,
        time=time,
    )
    task_uuid = task["task_id"]

    logger.debug(f"Start waiting for task {task_uuid} to finish")
    task_status = get_task_status(task_uuid)
    processing = True
    while processing:
        task_status = get_task_status(task_uuid)
        if task_status in ("PENDING", "UNKNOWN", "STARTED", "RETRY"):
            logger.debug(f"Still waiting for task {task_uuid}")
            sleep(5)
        elif task_status == "SUCCESS":
            logger.debug("Task completed")
            sleep(5)
            download_url = get_task_download_url(task_uuid)
            return download_url
        else:
            logger.debug("Task failed")
            return None


def get_static_rasters_links(
    static_rasters, projection=None, resolution=None, bbox=None, time=None
):
    """return a dict of urls to geotiff files of static rasters in scenario
    the dict items are formatted as result_name: link.tif.
    Time format is '%Y-%m-%dT%H:%M:%SZ'."""
    static_raster_urls = {}
    for static_raster in static_rasters:
        name = static_raster["name_3di"]
        static_raster_url = get_raster_download_link(
            raster=static_raster,
            # TODO: parameter scenario_instance is missing!
            projection=projection,
            resolution=resolution,
            bbox=bbox,
            time=time,
        )
        static_raster_urls[name] = static_raster_url
    return static_raster_urls


def get_temporal_raster_links(
    temporal_raster,
    projection=None,
    resolution=None,
    bbox=None,
    interval_hours=None,
):
    """return a dict of urls to geotiff files of a temporal raster
    the dict items are formatted as name_3di_datetime: link.tif"""
    temporal_raster_urls = {}
    name = temporal_raster["name_3di"]
    timesteps = get_raster_timesteps(
        raster=temporal_raster, interval_hours=interval_hours
    )
    for timestep in timesteps:
        download_url = get_raster_download_link(
            raster=temporal_raster,
            # TODO: parameter scenario_instance is missing!
            projection=projection,
            resolution=resolution,
            bbox=bbox,
            time=timestep,
        )
        if timestep is None:
            # Should not happen, but makes the code checker happy that
            # None.split() won't happen :-)
            raise ValueError("Timestep 'None' found, indicating non-temporal raster")
        url_timestep = os.path.splitext(download_url)[0].split("_")[-1]
        # Lizard returns the nearest timestep based on the timestep request
        timestep_url_format = "{}Z".format(timestep.split(".")[0].replace("-", ""))
        if timestep_url_format == url_timestep:
            # when requested and retrieved timesteps are equal, use timestep
            name_timestep = "_".join([name, timestep])
        else:
            # if not equal, indicate the datetime discrepancy in file name
            name_timestep = f"{name}_get_{timestep_url_format}_got_{url_timestep}"
        temporal_raster_urls[name_timestep] = download_url
    return temporal_raster_urls


def get_temporal_rasters_links(
    temporal_rasters,
    projection=None,
    resolution=None,
    bbox=None,
    interval_hours=None,
):
    """get links to all temporal rasters"""
    temporal_rasters_urls = {}
    for temporal_raster in temporal_rasters:
        temporal_raster_urls = get_temporal_raster_links(
            temporal_raster=temporal_raster,
            projection=projection,
            resolution=resolution,
            bbox=bbox,
            interval_hours=interval_hours,
        )
        for name_timestep, download_url in temporal_raster_urls.items():
            temporal_rasters_urls.setdefault(name_timestep, download_url)
    return temporal_rasters_urls


def to_datetime_obj(time_string):
    """returns a list of '%Y-%m-%dT%H:%M:%SZ'
    formatted timesteps in temporal range of raster object"""
    if "." in time_string:
        # If the timestamp contains milliseconds
        datetime_obj = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S.%fZ")
    else:
        # If the timestamp does not contain milliseconds
        datetime_obj = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%SZ")

    return datetime_obj


def get_raster_timesteps(raster, interval_hours=None):
    """returns a list of '%Y-%m-%dT%H:%M:%SZ' formatted timesteps in temporal
    range of raster object
    Starts at first timestep and ends at last timestep.
    The intermediate timesteps are determined by the interval.
    When no interval is provided, the first, middle and last timesteps are
    returned
    """
    raster_uuid = raster["uuid"]
    if not raster["temporal"]:
        return [None]
    if not interval_hours:
        # assume interval of store (rounded minutes) and return first, middle and last raster
        url = f"{LIZARD_URL}rasters/{raster_uuid}/timesteps/"
        timesteps_json = request_json_from_url(url)
        timesteps_ms = timesteps_json["steps"]
        # only return first, middle and last raster
        timesteps_ms = [
            timesteps_ms[0],
            timesteps_ms[round(len(timesteps_ms) / 2)],
            timesteps_ms[-1],
        ]
        timestep_obj_list = [
            to_datetime_obj(time_string) for time_string in timesteps_ms
        ]

        # Format the datetime object
        timesteps = [
            timestep_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
            for timestep_obj in timestep_obj_list
        ]

    else:
        # use interval from argument
        first_timestamp = raster["first_value_timestamp"]
        first_timestamp = to_datetime_obj(first_timestamp)

        last_timestamp = raster["last_value_timestamp"]
        last_timestamp = to_datetime_obj(last_timestamp)

        interval = timedelta(hours=interval_hours)

        timestep_obj_list = []

        while last_timestamp > first_timestamp:
            timestep_obj_list.append(first_timestamp)
            first_timestamp += interval

        if last_timestamp not in timestep_obj_list:
            timestep_obj_list.append(last_timestamp)

        timesteps = [
            timestep_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
            for timestep_obj in timestep_obj_list
        ]
    return timesteps


def get_raster_from_json(scenario_json, raster_code, subendpoint=None) -> dict:
    """return raster json object from scenario"""
    scenario_uuid = scenario_json["uuid"]
    raster_url = get_raster_url(scenario_uuid=scenario_uuid, raster_code=raster_code)

    r = requests.get(
        url=raster_url,
        auth=("__key__", get_api_key()),
    )

    r.raise_for_status()

    raster = r.json()
    return raster


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    return start <= x <= end


def check_temporal_request(scenario_instance, time):
    start_stamp = scenario_instance["simulation_start"]
    end_stamp = scenario_instance["simulation_end"]

    start = to_datetime_obj(start_stamp)
    end = to_datetime_obj(end_stamp)
    requested_time = to_datetime_obj(time)

    if not time_in_range(start, end, requested_time):
        raise ValueError(
            f"Time requested ({time}) not in temporal range of scenario "
            f"({start_stamp} - {end_stamp}), choose a different time."
        )


def request_json_from_url(url, params=None) -> dict:
    """retrieve json object from url"""
    r = requests.get(url=url, auth=("__key__", get_api_key()), params=params)
    r.raise_for_status()
    return r.json()


def resume_download_tasks(task_file, overwrite=False):
    """read csv with tasks and resume downloading the succesfull tasks"""

    processed_tasks = []
    unprocessed_tasks = []

    # Read tasks from file
    with open(task_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            unprocessed_tasks.append(row)
            task_url = row["url"]
            logger.debug(f"Reading task file, line: {task_url}")

    while len(unprocessed_tasks) > 0:
        for task in unprocessed_tasks:
            uuid = task["uuid"]
            pathname = task["pathname"]

            task_status = get_task_status(uuid)

            if task_status == "SUCCESS":
                # Task succesfull, check if file already exists

                # Download if it doesn't exist, or if it do
                if not os.path.isfile(pathname) or overwrite:
                    try:
                        download_task(task_uuid=uuid, pathname=pathname)
                    except HTTPError as err:
                        if err.code == 503:
                            logger.debug(
                                "503 Server Error: Lizard has lost it.Let's ignore this."
                            )
                            task_status = "UNKNOWN"
                        else:
                            raise

                # move task to processed list
                processed_tasks.append(task)
                unprocessed_tasks.remove(task)

            elif task_status in ("PENDING", "UNKNOWN", "STARTED", "RETRY"):
                pass
            else:
                logger.debug(f"Task {uuid} failed, status was: {task_status}")
        sleep(5)
