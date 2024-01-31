#!/usr/bin/env python3
import shapely
from shapely.geometry.base import BaseGeometry

__all__ = ["closing", "opening", "erode", "erosion", "dilate", "dilation", "close"]

from warg import passes_kws_to

FALLBACK_CAPSTYLE = shapely.BufferCapStyle.round  # CAN BE OVERRIDEN


@passes_kws_to(shapely.geometry.base.BaseGeometry.buffer)
def erosion(
    geom: BaseGeometry,
    distance: float = 1e-7,
    cap_style: shapely.BufferCapStyle = shapely.BufferCapStyle.flat,
    join_style: shapely.BufferJoinStyle = shapely.BufferJoinStyle.mitre,
    **kwargs
) -> BaseGeometry:
    """

    :param distance:
    :param cap_style:
    :param join_style:
    :param geom: The geometry to be eroded
    :return: The eroded geometry
    """
    return geom.buffer(
        distance=-distance, cap_style=cap_style, join_style=join_style, **kwargs
    )


@passes_kws_to(shapely.geometry.base.BaseGeometry.buffer)
def dilation(
    geom: BaseGeometry,
    distance: float = 1e-7,
    cap_style: shapely.BufferCapStyle = shapely.BufferCapStyle.flat,
    join_style: shapely.BufferJoinStyle = shapely.BufferJoinStyle.mitre,
    **kwargs
) -> BaseGeometry:
    """

    :param cap_style:
    :param join_style:
    :param geom: The geometry to be dilated
    :param distance: Dilation amount
    :return: The dilated geometry
    """
    if (
        isinstance(geom, shapely.Point) and cap_style == shapely.BufferCapStyle.flat
    ):  # NONSENSE, propably not what is intended
        cap_style = FALLBACK_CAPSTYLE

    return geom.buffer(
        distance=distance, cap_style=cap_style, join_style=join_style, **kwargs
    )


@passes_kws_to(shapely.geometry.base.BaseGeometry.buffer)
def closing(geom: BaseGeometry, **kwargs) -> BaseGeometry:
    """

    :param geom: The geometry to be closed
    :return: The closed geometry
    """
    return erode(dilate(geom, **kwargs), **kwargs)


@passes_kws_to(shapely.geometry.base.BaseGeometry.buffer)
def opening(geom: BaseGeometry, **kwargs) -> BaseGeometry:
    """

    :param geom: The geometry to be opened
    :return: The opened geometry
    """
    return dilate(erode(geom, **kwargs), **kwargs)


# open = opening # keyword clash
erode = erosion
dilate = dilation
close = closing

if __name__ == "__main__":

    def aishdjauisd():
        # Import constructors for creating geometry collections
        from shapely.geometry import MultiPoint, MultiLineString

        # Import necessary geometric objects from shapely module
        from shapely.geometry import Point, LineString, Polygon

        # Create Point geometric object(s) with coordinates
        point1 = Point(2.2, 4.2)
        point2 = Point(7.2, -25.1)
        point3 = Point(9.26, -2.456)
        # point3D = Point(9.26, -2.456, 0.57)

        # Create a MultiPoint object of our points 1,2 and 3
        multi_point = MultiPoint([point1, point2, point3])

        # It is also possible to pass coordinate tuples inside
        multi_point2 = MultiPoint([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])

        # We can also create a MultiLineString with two lines
        line1 = LineString([point1, point2])
        line2 = LineString([point2, point3])
        multi_line = MultiLineString([line1, line2])
        polygon = Polygon([point2, point1, point3])

        from shapely.geometry import GeometryCollection
        from matplotlib import pyplot
        import geopandas

        geoms = GeometryCollection([multi_point, multi_point2, multi_line, polygon])

        # A positive distance produces a dilation, a negative distance an erosion. A very small or zero distance may sometimes be used to “tidy” a polygon.
        geoms = opening(geoms)
        geoms = dilate(geoms)
        geoms = closing(geoms)
        geoms = erode(geoms)

        p = geopandas.GeoSeries(geoms)
        p.plot()
        pyplot.show()

    aishdjauisd()
