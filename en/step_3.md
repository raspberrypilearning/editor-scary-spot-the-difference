<h2 class="c-project-heading--task">Swap to a scary image</h2>
--- task ---

Swap images after 5 seconds.

--- /task ---

Calculate how long the program has been running and show the scary image when 5 seconds have passed.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 19
line_highlights: 20-26
---
def draw():
    elapsed = time() - start_time
    if elapsed < 5:
        # Show spot the difference image
        image(spot_diff_img, 0, 0, width, height)
    else:
        # Time for a scare!
        image(scary_img, 0, 0, width, height)
--- /code ---

</div>

<div class="c-project-output">

<pre>You should see a scary image after 5 seconds.</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

- `elapsed` will let us decide when to swap images.

</div>

