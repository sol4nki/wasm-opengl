# What a computer screen actually is (pixels, buffers)

>Lesson Goal - To properly understand what a screen is composed of and how it works, not as a magic box that displays anything.

## 1. The naïve idea (and why it’s wrong)

Most beginners dont really understand how the screen displays stuff, to them it doesnt really matter because *"its more of a hardware issue"* but that is not the case, hardware needs to talk to some kind of software to display anything on the screen.

Graphical programming will become confusing when you dont really know *what you're actually writing to*.

I'll try to demistify this *enigma* in the following lessons.

## 2. The correct idea: Grid of Pixels

At the lowest useful level, a screen is a grid of many small units called **PIXELS**.

For example: `1920x1080` means `1920` pixels in a row and `1080` in a column placed like a grid so total `207360` pixels on your screen.

```yaml
<<<     1920 pixels wide.    >>>
┌──────────────────────────────┐
│ █ █ █ █ █ █ █ █ █ █ █ █ █ █ │ ↑
│ █ █ █ █ █ █ █ █ █ █ █ █ █ █ │ 1080 pixels tall
│ █ █ █ █ █ █ █ █ █ █ █ █ █ █ │ ↓
└──────────────────────────────┘
```
And each of these pixels stores color information in a certain format usually **RGBA**.


## 3. What is a pixel, exactly?

A pixel is **not** a shape.
It is **data**.

Most commonly a pixel is stored as four numbers:
```css
 (R, G, B, A)

> R – red intensity
> G – green intensity
> B – blue intensity
> A – alpha (opacity)
```
and each of these values is usually 8 bits (0–255).
<div style="text-align: center;">
  <img src="img/what_pixels.png" alt="pixels displayed">
</div>

so pixels might be:
```css
(255, 0, 0, 255) -> solid red
(0, 0, 0, 255)   -> black
(255, 255, 255, 255) -> white
(255, 255, 0, 0) -> transparent
```

## 4. Where do these pixel values live?

This is the most important idea of this lesson.
> Pixels live in memory

Specifically, in a **contiguous block of memory** called a **FRAMEBUFFER**.

Think of it like this:
```yaml
      Memory (RAM or VRAM)
┌────────────────────────────┐
│ Pixel 0  → (R,G,B,A)       │
│ Pixel 1  → (R,G,B,A)       │
│ Pixel 2  → (R,G,B,A)       │
│ ...                        │
│ Pixel (width × height - 1) │
└────────────────────────────┘
```

So, the screen hardware is continously reading this so called *framebuffer* to draw what you see on your screen. The number of times it reads it per second depends on the screen Hertz example `60Hz` means `60 times in one second` and `144Hz` means `144 times per second`.

## 5. The screen does NOT know about shapes

So this one must be clear by now, The screen doesnt know anything other than pixel data so all the:

- Circles
- Triangles
- Cubes
- Lines
- ...

Are just the software telling the frame buffer that `pixel(x,y)` has this *RGBA* configuration. 

And everything in graphics exists to make this conversation efficient and faster

## 6. How images appear: scan-out

So the hardware does something like this again and again (depending on the screen refresh rate in `Hz` as told earlier)
```py
for y = 0 -> height
  for x = 0 -> width
    read pixel(x, y) from framebuffer
    emit the lights with those rgba intensities
```
This is why:
- updating memory updates the screen
- corrupted memory = visual glitches and issues
- various other issues we'll cover later

## 7. Important separation!

At This this level there are 3 seperate things:

```yaml
[ Pixel Memory ] -> [ Display Hardware ] -> [ Your Eyes ]
```

Your program will never talk to hardware directly it will just write to memory.

Now,
- the **GPU** helps fillout the memory
- and **WebGL/OpenGL** defines how the **GPU** should fill the memory
- the **Browser/OS** decides where the memory appears

But the core idea never changes.

## 8. Why any of this matters

When you render anything using opengl+emscripten in the browser:
- you won't be drawing a cube
- you will be calculating `pixel(x,y)` colors

The entire pipeline goes like this 
```yaml
cube -> triangles -> pixels -> framebuffer -> screen
```

## Recap

- A screen is just a grid of pixels
- Pixels are just data usually RGBA
- Pixel data lives in framebuffer (memory)
- Screen hardware reads the framebuffer to display stuff on screen
- Screen knows nothing about shapes, it only knows pixel(x,y) data
- All graphics programming exists to fill pixel memory efficiently