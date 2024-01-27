threedi-scenario-downloader
==========================================

The threedi-scenario-downloader package includes functions in order to
automate most used download actions on the 3Di results.

Example methods are:

- Download raw results.
- Download logging.
- Download maximum waterdepth (non-temporal raster).
- Download waterdepth (temporal raster, supply timestamp for snapshot).
- Find all scenarios model slug or scenario name.

Examples
--------

Start importing the package::

  >>> from threedi_scenario_downloader import downloader as dl

Set the API key for authentication to the Lizard API (you can get an API key
here: <your portal>.lizard.net/management/#/personal_api_keys)::

  >>> dl.set_api_key("INSERT YOUR API KEY HERE")

Find scenarios based on a model slug (unique model identifier) or scenario
name. Returns last 10 matching results unless told otherwise::

  >>> scenarios = dl.find_scenarios_by_model_slug("enter your model_uuid", limit=10)

or::

  >>> scenarios = dl.find_scenarios_by_name("my_first_scenario", limit=100)

or if you have too many similarly-named scenarios, do a case-sensitive exact
search::

  >>> scenarios = dl.find_scenarios_by_exact_name("my_first_scenario", limit=100)

Do you want to download the raw 3Di-results (.nc and .h5 files) of a specific
scenario? Use the following methods::

  >>> dl.download_raw_results("scenario_uuid")
  >>> dl.download_grid_administration("scenario_uuid")

or::

  >>> dl.download_raw_results("scenario_uuid",pathname="save_under_different_name.nc")
  >>> dl.download_grid_administration("scenario_uuid",pathname="save_under_different_name.h5")

Downloading (temporal) rasters of specific scenarios can be done using the
following methods::

  >>> dl.download_maximum_waterdepth_raster("scenario_uuid",projection="EPSG:28992",resolution=10)
  #download the full extent of the maximum waterdepth of the given scenario_uuid with a 10 meter resolution in the RD New/Amersfoort projection (EPSG:28992)

  >>> dl.download_waterdepth_raster("scenario_uuid",projection="EPSG:28992",resolution=10,time="2019-01-01T02:00")
  #download the full extend of the waterdepth at the supplied timestamp given scenario_uuid, on 10 meter resolution in the RD New/Amersfoort projection (EPSG:28992)

The raster download methods creates a task for the API. Depending on the size
and resolution it takes some time for the raster to be prepared. These methods
will keep on checking if the raster is ready to be downloaded.  When a raster
is ready to be downloaded a message in the Lizard portal is created as
well. If you want to delete these messages (due to bulk downloading for
example), use the following method::

  >>> dl.clear_inbox()


Installation
------------

We can be installed with::

  $ pip install threedi-scenario-downloader


Development installation of this project itself
-----------------------------------------------

We're installed with regular pip and virtualenv. Create a virtualenv and call pip::

  $ python3 -m venv venv
  $ venv/bin/pip install -r requirements.txt

In order to get nicely formatted python files without having to spend
manual work on it, run the following commands periodically::

  $ venv/bin/ruff check threedi_scenario_downloader --fix
  $ venv/bin/ruff format threedi_scenario_downloader

The first one also reports syntax-like errors that you'll have to fix.

Run the tests regularly. This also checks reports coverage::

  $ venv/bin/pytest

Before running the tests, create a file (in this directory) called
``test_api_key.txt`` and add a lizard **api key**. Just the key, on
one line. The tests will complain otherwise. In the github action,
this .txt file is filled with the ``TEST_API_KEY`` github secret.

Contact Reinout when you need a new release, there's no automatic
upload to pypi yet so he has to upload it.

If you need a new dependency (like `requests`), add it in `setup.py` in
`install_requires`. Afterwards, run install again to actuall install your
dependency::

  $ venv/bin/pip install -r requirements.txt
