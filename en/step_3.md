<h2 class="c-project-heading--task">Make it random</h2>

Your program is predictable.

<h2 class="c-project-heading--explainer">Follow these instructions</h2>

Add randomness by changing the pause between the two images being displayed.


Change the pause between the two images being on screen to the `scare_delay`, which is currently set using `randrange` to a random value between 5 and 14.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 19
line_highlights: 21
---
def draw():
    elapsed = time() - start_time
    if elapsed < scare_delay:
        # Show spot the difference image
        image(spot_diff_img, 0, 0, width, height)
    else:
        # Time for a scare!
        image(scary_img, 0, 0, width, height)
--- /code ---
</div>

<div class="c-project-output">
<pre>You should see a scary image after a random delay of between 5 and 14 seconds.</pre>
</div>

### Tip

<div class="c-project-callout c-project-callout--tip">

- The second value in `randrange` is not included in the range, so this is why the maximum delay is 14, not 15 seconds.

</div>

## Now run your code

Run your code and check that the scary image appears after a random delay.
