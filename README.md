# ua-generator

A random user-agent generator for Python >= 3.6

# Features
* No external user-agent list. No downloads.
* Templates are hardcoded into the code.
* Platform and browser versions are based on real releases.
* Client hints (Sec-CH-UA fields).

# Installing
```bash
pip3 install -U ua-generator
```

# Basic usage

```python
import ua_generator

ua = ua_generator.generate()
print(ua) # Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/15.2 Safari/604.1.38
```

# Customization
**There are three different parameters to the generate user-agent by the certain conditions.**

```python
device = ('desktop', 'mobile')
platform = ('windows', 'macos', 'ios', 'linux', 'android')
browser = ('chrome', 'edge', 'firefox', 'safari')
```
*All of the parameters are optional, and the types can be set multiple times by using a tuple.*

## Customized user-agent generation:
```python
import ua_generator

# Example 1:
ua = ua_generator.generate(device='desktop', browser=('chrome', 'edge'))
print(ua.text) # Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.145 Safari/537.36
print(ua.platform) # windows
print(ua.browser) # chrome
print(ua.ch.brands) # "Not A(Brand";v="99", "Chromium";v="108", "Google Chrome";v="108"
print(ua.ch.mobile) # ?0
print(ua.ch.platform) # "Windows"
print(ua.ch.platform_version) # "10.0"

# Example 2:
ua = ua_generator.generate(platform=('ios', 'macos'), browser='chrome')
print(ua.text) # Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) CriOS/119.0.6045.176 Mobile/15E148 Safari/537.36
print(ua.platform) # ios
print(ua.browser) # chrome
print(ua.ch.brands) # "Not A(Brand";v="99", "Chromium";v="119", "Google Chrome";v="119"
print(ua.ch.mobile) # ?1
print(ua.ch.platform) # "iOS"
print(ua.ch.platform_version) # "17.0.2"
```

# Headers
```python
ua = ua_generator.generate(browser=('chrome', 'edge'))

# This will return a dictionary containing the generated user-agent:
print(ua.headers.get())
{
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.43 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Chromium";v="103", "Google Chrome";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"'
}

# Extending the "Client Hints" by a value of the "Accept-CH" header:
print(ua.headers.accept_ch('Sec-CH-UA-Platform-Version, Sec-CH-UA-Full-Version-List'))
print(ua.headers.get())
{
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Safari/537.36',
    'sec-ch-ua': '"Not A(Brand";v="99", "Chromium";v="122", "Google Chrome";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '"14.1.0"',
    'sec-ch-ua-full-version-list': '"Not A(Brand";v="99", "Chromium";v="122.0.6261.94", "Google Chrome";v="122.0.6261.94"'
}
```

## Integrating into the [requests](https://pypi.org/project/requests/):
```python
import requests
import ua_generator

ua = ua_generator.generate(browser=('chrome', 'edge'))
r = requests.get("https://httpbin.org/get", headers=ua.headers.get())
print(r.text)
```

# Issues
You can create an issue [from here](https://github.com/iamdual/ua-generator/issues) if you are experiencing a problem. 

# Author
Ekin Karadeniz (iamdual@icloud.com)