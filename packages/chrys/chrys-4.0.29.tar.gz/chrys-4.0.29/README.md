# chrys

[![CircleCI](https://circleci.com/gh/netbek/chrys.svg?style=svg)](https://circleci.com/gh/netbek/chrys)

A collection of color palettes for visualisation in JavaScript, Python and Sass.

## Demo

[netbek.github.io/chrys](https://netbek.github.io/chrys#colour-schemes)

## Installation

### Node.js and Sass

```shell
npm install chrys
```

### Python 3.6 and up

```shell
pip install chrys
```

## Usage

For instructions, refer to [the docs](https://netbek.github.io/chrys#usage).

## Development: Installation

1. Build the Docker container:

    ```shell
    ./docker/install.sh
    ```

2. Create `.pypirc`:

    ```shell
    cp example.pypirc .pypirc
    ```

3. Enter a [PyPI API token](https://pypi.org/manage/account/#api-tokens) as the password in `.pypirc`.

## Development: Usage

Upgrade Node dependencies:

```shell
./docker/run.sh ./docker/scripts/upgrade_node_deps.sh
```

Build the palette data, JavaScript and Python distribution packages, Sass, CSS, Illustrator scripts:

```shell
./docker/run.sh ./docker/scripts/build.sh
```

Publish the JavaScript and Python distribution packages:

```shell
npm publish
npm run publish-py
```

## Credit

Palettes from:

* [Bokeh](https://github.com/bokeh/bokeh) (BSD 3-Clause)
* [Vega](https://github.com/vega/vega) (BSD 3-Clause)

## License

Copyright (c) 2017 Hein Bekker. Licensed under the BSD 3-Clause License.
