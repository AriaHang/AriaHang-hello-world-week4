
from tkinter import Tk, Canvas, BOTH
from math import sin, cos, pi
from PIL import ImageGrab

# Color palette
palette = [
    "#00D9FF",  # Cyan
    "#40F5C8",  # Mint
    "#FFE66D",  # Yellow
    "#FF8A5B",  # Orange
    "#FF4FA3",  # Pink
]

# Artwork settings
count = 800
scale_factor = 10
origin_x = 300
origin_y = 300

# Golden angle
phi = (1 + 5**0.5) / 2
angle_increment = (2 - phi) * 2 * pi

# Create window
app = Tk()
app.title("Chaotic Bloom")
app.geometry("600x600")

canvas = Canvas(
    app,
    bg="#101820",
    highlightthickness=0
)
canvas.pack(fill=BOTH, expand=True)

# Animation variables
j = 1
theta = 0


def grow():
    global j, theta

    if j <= count:
        # Spiral position
        r = scale_factor * j**0.5
        theta += angle_increment

        # Organic wave distortion
        wave = 1 + 0.22 * sin(theta * 5)

        x = origin_x + r * wave * cos(theta)
        y = origin_y + r * wave * sin(theta)

        # Circle size increases outward
        size = 3 + (j / count) * 16

        # Color changes as the spiral grows
        color = palette[(j // 35) % len(palette)]

        # Draw circle
        canvas.create_oval(
            x, y,
            x + size, y + size,
            fill=color,
            outline=""
        )

        # Continue animation
        j += 1
        app.after(15, grow)

    else:
        # Save the completed artwork
        app.update_idletasks()

        x = canvas.winfo_rootx()
        y = canvas.winfo_rooty()
        width = canvas.winfo_width()
        height = canvas.winfo_height()

        ImageGrab.grab(
            bbox=(x, y, x + width, y + height)
        ).save("chaotic-bloom.png")

        print("Artwork saved!")


# Start animation
grow()
app.mainloop()
