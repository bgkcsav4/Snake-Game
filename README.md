# Snake‑Game

A minimalist **Python 3** implementation of the classic *Snake* arcade game that **renders each frame to an image file** instead of using `pygame` or the terminal. This approach lets you stitch the frames into a GIF, stream them to the web, or inspect the board step‑by‑step for unit testing.

> *“Snake Game but generates the image”* 

## Features

|    | Capability                                                               |
| -- | ------------------------------------------------------------------------ |
| 🖼 | Generates a **PNG** (or JPEG) for every tick—great for GIFs or debugging |
| 🎯 | Arrow‑key controls via `keyboard` module (fallback to WASD)              |
| 🍎 | Random food spawns & self‑collision detection                            |
| ⚙️ | Configuration flags for board size, speed (FPS), output folder           |
| 📦 | Zero external dependencies beyond **Pillow** (image) + **keyboard**      |


## Project Structure

```
Snake-Game/
├─ program01.py        # All game logic + image rendering
├─ data/               # (Optional) pre‑rendered assets, e.g. apple.png
└─ docs/
   └─ demo.gif         # Example output
```

> The **`data/`** folder is optional; if the sprites are missing the script falls back to drawing simple coloured rectangles.

---

## How It Works

1. **Game Loop** – A `while running:` loop updates the head position based on the current direction every `1/fps` seconds.
2. **State Mutations** – Food consumption triggers tail growth and a random re‑spawn (`random.randint`). Self‑collision sets `running = False`.
3. **Rendering** – For each tick, `Pillow.Image.new()` creates a blank canvas. Squares are drawn via `ImageDraw.rectangle` and saved as `frames/{step:04d}.png`.
4. **Input** – `keyboard.on_press_key()` registers a callback that updates the direction variable; input is non‑blocking so rendering stays smooth.
5. **Cleanup** – Upon exit, the script prints the final score and suggests stitching the frames into a video/GIF.

