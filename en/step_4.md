<h2 class="c-project-heading--task">Make it random</h2>
--- task ---
Your program is predictable. 
Add randomness by changing the pause between the two images being displayed.
--- /task ---

Change the `sleep` pause between the two images being on screen to a random number.

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
<pre>You should see a scary image after a random delay of between 5 and 15 seconds.</pre>
</div>
