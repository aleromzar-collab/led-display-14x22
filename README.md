# LED Display 14x22

Genera un display LED 14×22 y permite insertar una o varias submatrices (0/1)
indicando la posición (fila, columna) de la esquina superior izquierda.

- Encendido: blanco
- Apagado: negro
- Fondo: gris

## Instalación
pip install -r requirements.txt

## Ejemplo
```python
from led_display import render_led_display_14x22

digit_1 = [
  [0,0,1,1,1],
  [0,1,1,1,1],
  [1,1,1,1,1],
]

grid, img = render_led_display_14x22([
    (digit_1, (0, 8))
])

img

