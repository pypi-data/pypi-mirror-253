# PyShlink
Python module for API communication with [Shlink](https://shlink.io)

This package is based on the work of David Southgate and his creation, shlink-py, which you can find here: [shlink-py](https://github.com/DavidSouthgate/shlink-py)

## Installation
To install simply use pip:

```bash
pip install shlink
```

## Usage
This package is designed with the intention of extracting information from the Shlink API, using version 3 of the API. The package contains three main functions derived from operations that can be performed using short URLs or visits to short URLs.

Below is an example showcasing all the operations currently available:

```python
from shlink import Shlink

shlink_url = 'https://s.shlink.example/'
shlink_api_key = 'this_is_a_veryvery_large_apikey_for_shlink'

# Connect to Shlink API
shlink = Shlink(url=shlink_url, api_key=shlink_api_key)

# List of short URLs
short_urls = shlink.list_short_urls()

# Get the short URL from a provided shortCode
get_short_url = shlink.get_short_url('shortCode')

# Information of each visit from a provided shortCode 
visits_data = shlink.list_visit_data('shortCode')
```
It's also crucial to emphasize that within the visit information, you will find the 'userAgent' information, presented in the following format:

```
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 .0.0 Safari/537.36
```

To extract valuable information from 'userAgent,' the installation of the 'user_agents' package is required. It's important to highlight that this step is necessary only if you intend to extract details from visits, specifically information like the browser, operating system, or device from each visit.

Below is how to use the user_agents package:

```python
!pip install user-agents

from user_agents import parse

# Example of a userAgent string 
user_agent_string = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

ua = parse(user_agent_string)

# Extract details
browser_name = ua.browser.family
browser_version = ua.browser.version_string
os_name = ua.os.family
os_version = ua.os.version_string
device = ua.device.family

# Print the extracted information
print(f"Browser: {browser_name} {browser_version}")
print(f"Operating System: {os_name} {os_version}")
print(f"Device: {device}")
```

