<h2 class="c-project-heading--task">Change the range</h2>

### Step 1

The range of seconds used for the delay is set in the `preload()` function.


Alter the values in `randrange`.

We have changed it to `randrange(3, 8)`, to generate values between 3 and 7.

Experiment with your own ranges.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 6
line_highlights: 12
---
def preload():
    global spot_diff_img, scary_img
    global start_time, scare_delay
    spot_diff_img = load_image("spot_the_diff.png")
    scary_img = load_image("scary_face.png")
    start_time = time()
    scare_delay = randrange(3, 8)
--- /code ---
</div>

<div class="c-project-output">
<pre>You should see a scary image after a random delay in the range of seconds you set.</pre>
</div>

Well done! you have completed the project!
