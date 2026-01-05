# What the GPU is and why it exists

>Lesson Goal - To understand what the GPU is, why it exists and why we cant just use CPU to compute graphics.

## 1. Restating the big picture from Lesson-1

From Lesson-1 we know that:
- every screen is just a grid of pixels
- to show anything framebuffer needs to be filled
- and every frame = millions of pixels

For example: 
- `1920x1080` is approxmiately 2million+ pixels
- at `60Hz` it becomes 
    ```py
    2,000,000 * 60 = 120million pixels per second (approx)
    ```
- and each of these pixels needs its color computed

And this huge number is the key to understanding why **GPUS** are actually needed

## 2. The CPU problem

CPU is important, very important indeed but its designed to be:
- Very Smart
- Very Flexible
- Very fast at serial and branching logic

But like all good things it also has its limits.

### How a CPU thinks:
A CPU core is good at 
```yaml
do, abc task
then, do pqr task
if pqr doesnt happen, branch
handle OS, input, logic, AI, physics and much more
```

And here comes the drawbacks of a CPU:
- has only a few cores (usually 4-16, can vary depending on manufacturing company, models etc.)
- Very complex control logic
- Expensive context switching (refers to the significant time, productivity, and energy lost when switching between tasks)

Now just imagine asking the cpu:

> *"For every pixel(x,y) on the screen read the framebuffer X-times per second, do the math and figure out the colors"* 

Basically repeating the same operation X-times per second (where X is the refresh rate of the screen)

This is the **WORST** possible workload for a CPU.

## 3. The key observation that led to GPUs

Early Engineers realized something critical:

> Pixel and vertex calculations are massively parallel

>[!NOTE]
> will be continued soon
## 4. The GPU’s purpose (in one sentence)
## 5. How a GPU is different from a CPU
## 6. What the GPU actually computes
## 7. The GPU does NOT “know” about objects
## 8. Where the GPU fits in the system (important diagram)
## 9. Why this matters for OpenGL and WebGL
## Recap
