# wasm-opengl

> [!IMPORTANT]
> This is under development! i am still skimming through various resources to make proper modules

> [!TIP]
> Any queries/improvements are appreciated you can contact me on discord!

Hello there, this is a collection of 9 modules that will help you get a grasp of modern emscripten and opengl integration, starting from **SCRATCH**, you dont require any prior knowledge except some basic arithmetic and C/CPP (although this couse will follow C).

All the modules with their contents are listed below, you can have a look and skip to the relevant section! 

HAPPY LEARNING !!


<!-- yes "py", py looks nice so i am adding it -->
```py
PHASE 0 — Foundations (no code)
1. What a computer screen actually is (pixels, buffers)
2. What the GPU is and why it exists
3. CPU vs GPU responsibilities
4. What “real-time rendering” means
5. What a frame is and what a frame loop is
```
```py
PHASE 1 — Graphics mental model
6. What OpenGL actually is
7. What OpenGL is NOT
8. Why OpenGL does not create windows
9. The concept of a graphics context
10. The rendering pipeline (CPU → GPU → screen)
```
```py
PHASE 2 — Shaders and data
11. Why shaders exist
12. What a vertex really is
13. What vertex buffers are and why they exist
14. How the GPU reads memory
15. What uniforms are and when they change
```
```py
PHASE 3 — Math (only what is necessary)
16. Coordinate systems
17. Why matrices exist
18. Model, View, Projection (intuitively first)
19. How a 3D cube is represented in memory
```
```py
PHASE 4 — Frame execution
20. Initialization vs per-frame work
21. What happens during ONE frame (step-by-step)
22. Why state exists in OpenGL
23. Common beginner mistakes in frame logic
```
```py
PHASE 5 — Desktop OpenGL as a learning sandbox
24. Why we use desktop OpenGL temporarily
25. What GLFW/SDL actually do (and what they don’t)
26. Minimal desktop OpenGL program structure
27. Writing renderer code that does NOT depend on the OS
```
```py
PHASE 6 — Emscripten & browser mapping
28. What WebAssembly actually is
29. What Emscripten does and does NOT do
30. How browser canvas replaces windows
31. How WebGL maps to OpenGL ES concepts
32. What changes when compiling to WASM
33. What does NOT change when compiling to WASM
```
```py
PHASE 7 — The actual project
34. Rendering a static triangle
35. Rendering a static cube
36. Adding depth
37. Making the cube rotate
38. Adding keyboard input
39. Making movement frame-rate independent
```
```py
PHASE 8 — Debugging & understanding
40. How to debug when nothing appears on screen
41. Typical beginner OpenGL errors
42. Mental checklist when something breaks
43. How to reason about rendering bugs
```


<!--
[!NOTE]
[!TIP]
[!IMPORTANT]
[!WARNING]
[!CAUTION]
-->
