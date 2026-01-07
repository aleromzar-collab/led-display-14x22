import numpy as np
from led_display import render_led_display_14x22

def test_output_grid_shape():
    sub = [
        [1, 0, 1],
        [0, 1, 0],
    ]
    grid, img = render_led_display_14x22([
        (sub, (0, 0))
    ])
    assert grid.shape == (14, 22)

def test_overlay_positioning():
    sub = [
        [1, 1],
        [1, 0],
    ]
    grid, _ = render_led_display_14x22([
        (sub, (5, 10))
    ])
    # Comprueba que se pegó en (5,10)
    assert grid[5, 10] == 1
    assert grid[5, 11] == 1
    assert grid[6, 10] == 1
    assert grid[6, 11] == 0

def test_multiple_overlays_or_behavior():
    a = [
        [1, 0],
        [0, 0],
    ]
    b = [
        [0, 1],
        [0, 0],
    ]
    grid, _ = render_led_display_14x22([
        (a, (3, 3)),
        (b, (3, 3)),
    ])
    # "OR": queda encendido si cualquiera lo enciende
    assert grid[3, 3] == 1
    assert grid[3, 4] == 1

def test_image_is_created():
    sub = [[1]]
    _, img = render_led_display_14x22([
        (sub, (0, 0))
    ])
    assert img.size[0] > 0 and img.size[1] > 0
