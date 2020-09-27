# keyboard
Script that pushes a button or moves the mouse randomly in a given timeframe so your laptop won't go to sleep.
For example when using Microsoft Teams, your status will go to idle after being afk for 5 minutes.

# how to run
From terminal:

```python
python -m keyboard.keyboard --min_time=30 --max_time=50
```

Or within a `.py` file:

```python
from keyboard.keyboard import do_keyboard

min_time = 10
max_time = 30
do_keyboard(min_time, max_time)
```