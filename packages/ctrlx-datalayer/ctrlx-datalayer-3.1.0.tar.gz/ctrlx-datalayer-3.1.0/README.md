# Python Wrapper for ctrlX Data Layer

This project provides ctrlX Data Layer access via Python.
It wraps the original ctrlX Data Layer written in C++.

## Setup

Set up a virtual python environment and install the packages libzmq5 and ctrlX Data Layer

```bash
sudo apt-get update && sudo apt-get -y install virtualenv libzmq5

DATALAYER_DEB_VERSION=2.4.5
SDK_RELEASE_VERSION=2.4.0

wget --quiet https://github.com/boschrexroth/ctrlx-automation-sdk/releases/download/${SDK_RELEASE_VERSION}/ctrlx-datalayer-${DATALAYER_DEB_VERSION}.deb \
    && sudo dpkg --install ctrlx-datalayer-${DATALAYER_DEB_VERSION}.deb \
    && rm ctrlx-datalayer-${DATALAYER_DEB_VERSION}.deb
    
virtualenv -p python3 venv && source venv/bin/activate
```
## Dependence On

  - supports flatbuffers >= v2

## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install ctrlX Data Layer.

```bash
pip3 install ctrlx-datalayer
```
## Usage

See [examples](https://boschrexroth.github.io/ctrlx-automation-sdk/)

## License

Python Wrapper for ctrlX Data Layer is licensed under [T&C](https://dc-corp.resource.bosch.com/media/xc/boschrexroth_tac_delivery.pdf) or see 'boschrexroth_tac_delivery.txt' as part of this package.