# Simple Brute-forcer
A simple brute-forcer.

### Example usage
```python
import brute_forcer
brute_forcer.chars = '123abc'
brute_forcer = brute_forcer.brute_forcer
z = brute_forcer()

while True:
    print('\r', next(z), end='')
    sleep(0.01)
```
