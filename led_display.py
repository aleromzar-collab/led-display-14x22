import numpy as np
from PIL import Image, ImageDraw
from typing import Sequence, Tuple

def render_led_display_14x22(
    overlays: Sequence[Tuple[Sequence[Sequence[int]], Tuple[int, int]]],
    *,
    grid_size=(14, 22),
    led_pitch=26,
    led_radius=10,
    margin=18,
    bg_color=(120, 120, 120),
    off_color=(0, 0, 0),
    on_color=(255, 255, 255),
    clamp=True
):
    H, W = grid_size
    grid = np.zeros((H, W), dtype=int)

    def paste(sub, top, left):
        sub = np.array(sub, dtype=int)
        sh, sw = sub.shape
        r0, c0 = top, left
        r1, c1 = r0 + sh, c0 + sw

        if clamp:
            rr0, cc0 = max(0, r0), max(0, c0)
            rr1, cc1 = min(H, r1), min(W, c1)
            if rr0 >= rr1 or cc0 >= cc1:
                return
            grid[rr0:rr1, cc0:cc1] = np.maximum(
                grid[rr0:rr1, cc0:cc1],
                sub[rr0-r0:rr1-r0, cc0-c0:cc1-c0]
            )
        else:
            if r0 < 0 or c0 < 0 or r1 > H or c1 > W:
                raise ValueError("Submatriz fuera de rango")
            grid[r0:r1, c0:c1] = np.maximum(grid[r0:r1, c0:c1], sub)

    for sub, (r, c) in overlays:
        paste(sub, r, c)

    img_w = margin*2 + (W-1)*led_pitch + 2*led_radius
    img_h = margin*2 + (H-1)*led_pitch + 2*led_radius
    img = Image.new("RGB", (img_w, img_h), bg_color)
    d = ImageDraw.Draw(img)

    for r in range(H):
        for c in range(W):
            color = on_color if grid[r, c] else off_color
            cx = margin + led_radius + c*led_pitch
            cy = margin + led_radius + r*led_pitch
            d.ellipse((cx-led_radius, cy-led_radius,
                       cx+led_radius, cy+led_radius), fill=color)

    return grid, img
