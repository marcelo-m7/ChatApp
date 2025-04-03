def handle_event(e: map.MapEvent):

def handle_tap(e: map.MapTapEvent):

def main(page: ft.Page):

ft.app(main)

import flet as ft
import flet.map as map

def main(page: ft.Page):
    my_map = map.Map(
        expand=True,
        initial_center=map.MapLatitudeLongitude(15, 10),
        initial_zoom=4.2,
        interaction_configuration=map.MapInteractionConfiguration(
            flags=map.MapInteractiveFlag.ALL
        ),
    )

    def zoom_in(e):
        my_map.zoom += 1
        page.update()

    def zoom_out(e):
        my_map.zoom -= 1
        page.update()

    page.add(
        ft.Row([
            ft.ElevatedButton(text="+", on_click=zoom_in),
            ft.ElevatedButton(text="-", on_click=zoom_out),
        ]),
        my_map,
    )

ft.app(main)

import flet as ft
import flet.map as map

def main(page: ft.Page):
    polyline_layer_ref = ft.Ref[map.PolylineLayer]()
    points = []

    def handle_tap(e: map.MapTapEvent):
        points.append(e.coordinates)
        polyline_layer_ref.current.polylines = [
            map.PolylineMarker(
                coordinates=points,
                color=ft.Colors.BLUE,
                border_stroke_width=2,
            )
        ]
        page.update()

    page.add(
        ft.Text("Click to add points to the polyline."),
        map.Map(
            expand=True,
            initial_center=map.MapLatitudeLongitude(15, 10),
            initial_zoom=4.2,
            interaction_configuration=map.MapInteractionConfiguration(
                flags=map.MapInteractiveFlag.ALL
            ),
            on_tap=handle_tap,
            layers=[
                map.TileLayer(url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png"),
                map.PolylineLayer(ref=polyline_layer_ref),
            ],
        ),
    )

ft.app(main)

import flet as ft
import flet.map as map
import random

def main(page: ft.Page):
    polygon_layer_ref = ft.Ref[map.PolygonLayer]()
    vertices = []

    def handle_double_tap(e: map.MapTapEvent):
        vertices.append(e.coordinates)
        if len(vertices) > 2:
            polygon_layer_ref.current.polygons.append(
                map.PolygonMarker(
                    coordinates=vertices[:],
                    color=ft.Colors.with_opacity(0.5, ft.Colors.GREEN),
                    border_color=ft.Colors.BLACK,
                    border_stroke_width=2,
                )
            )
            vertices.clear()
        page.update()

    page.add(
        ft.Text("Double-click to create a polygon vertex. Three vertices complete a polygon."),
        map.Map(
            expand=True,
            initial_center=map.MapLatitudeLongitude(15, 10),
            initial_zoom=4.2,
            interaction_configuration=map.MapInteractionConfiguration(
                flags=map.MapInteractiveFlag.ALL
            ),
            on_double_tap=handle_double_tap,
            layers=[
                map.TileLayer(url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png"),
                map.PolygonLayer(ref=polygon_layer_ref),
            ],
        ),
    )

ft.app(main)

import random
import flet as ft
import flet.map as map

marker_layer_ref = ft.Ref[map.MarkerLayer]()
circle_layer_ref = ft.Ref[map.CircleLayer]()
