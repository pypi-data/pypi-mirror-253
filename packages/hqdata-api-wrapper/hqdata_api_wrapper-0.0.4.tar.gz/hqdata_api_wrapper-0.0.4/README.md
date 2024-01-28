# HQData API Wrapper

[![PyPI Version](https://img.shields.io/pypi/v/hqdata-api-wrapper.svg)](https://pypi.org/project/hqdata-api-wrapper/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This is a Python package that provides a convenient wrapper for interacting with the HQData API. 
It allows you to easily run and fetch job/result data from the HQData service.

## Installation

You can install the package using pip:

```bash
pip install hqdata-api-wrapper
```

## Examples

Here's a simple example of how to use the `HQData` class from the `hqdata_api_wrapper` package:

```python
from hqdata_api_wrapper import HQData

# Create an instance of HQData worker
worker = HQData(apikey="your_api_key")
# Create an instance of HQData worker without debug prints and without autofetching / waiting for results
worker = HQData(apikey="your_api_key", autofetch=False, debug_messages=False)

# Example: list available modules and their fields
modules = worker.modules()
print(modules)

# Example: run scrape module
#module parameter = module name
#payload = dictionary of required/optional module fields
result = wroker.run(module="scrape", payload={"url": "https://hqdata.com", "contact_details": False, "recursive_contact_details": False, "pattern_scan": False, "js_scenario": "click://button[@aria-label='Example Xpath'];send_keys://input[@class='example']:Test Value;scroll:y:750"})

# Example: list jobs and optional filters
result = worker.fetch(page="2", status="success")

# Example: fetch result
result = worker.fetch(id=job_id)

# Example: fetch html of scraping job
result = worker.fetch(id=job_id, fetch="html")
```