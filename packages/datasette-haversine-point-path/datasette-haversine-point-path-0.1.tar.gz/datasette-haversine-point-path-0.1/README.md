# datasette-haversine-point-path
[![PyPI](https://img.shields.io/pypi/v/datasette-haversine-point-path.svg)](https://pypi.org/project/datasette-haversine-point-path/)
[![Changelog](https://img.shields.io/github/v/release/hcarter333/datasette-haversine-point-path?include_prereleases&label=changelog)](https://github.com/hcarter333/datasette-haversine-point-path/releases)
[![Tests](https://github.com/hcarter333/datasette-haversine-point-path/workflows/Test/badge.svg)](https://github.com/hcarter333/datasette-haversine-point-path/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/hcarter333/datasette-haversine-point-path/blob/main/LICENSE)

Datasette plugin that adds a custom SQL function for shortest haversine distances between a point and a path on a sphere

Install this plugin in the same environment as Datasette to enable the `haversine_point_path()` SQL function.
```bash
datasette install datasette-haversine-point-path
```
The plugin is built on top of the [haversine](https://github.com/mapado/haversine) library.

## haversine_point_path() to calculate distances

```sql
select haversine_point_path(lat1, lon1, lat2, lon2, lat3, lon3);
```

This will return the distance in kilometers between the path defined by `(lat1, lon1)`, `(lat2, lon2)`, and the point defined by `(lat3, lon3)`.

## Demo
No demo yet

## Custom units

By default `haversine_point_path()` returns results in km. You can pass an optional third argument to get results in a different unit:

- `ft` for feet
- `m` for meters
- `in` for inches
- `mi` for miles
- `nmi` for nautical miles
- `km` for kilometers (the default)

```sql
select haversine_point_path(lat1, lon1, lat2, lon2, 'mi');
```
