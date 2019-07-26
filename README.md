# Python-Polylabel
Port of polylabel library from MapBox

Official repo: [https://github.com/mapbox/polylabel](https://github.com/mapbox/polylabel)
Article - [https://www.mapbox.com/blog/polygon-center/](https://www.mapbox.com/blog/polygon-center/)

## Requirements
Python2.7+ or Python3+

## Installation

```
pip install python-polylabel
```

## Usage

```python

from polylabel import polylabel

polylabel([[[0, 0], [1, 0], [2, 0], [0, 0]]])  # [0, 0]

polylabel([[[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]], with_distance=True)  # ([0.5, 0.5], 0.5)

```

## Changelog

**0.6**
- fix problem with Queue on windows (support comparison on Cell class) [#5](https://github.com/Twista/python-polylabel/issues/5)

**0.5**
- add support for floats in polygon

**0.4**
- `with_distance` parameter, returns also distance

**0.3**
- python2 support
