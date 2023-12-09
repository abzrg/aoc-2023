# Advent Of Code - 2023

## Loop through regex group matches

```py
import re

pattern = re.compile(r'([A-Z]+)([0-9]+)')

# finditer: returns the matches one-by-one -> more memory efficient
for m in re.finditer(pattern, string):
    print m.group(2), '*', m.group(1)

# findall: returns a list of all results -> less memory efficient
for (letters, numbers) in re.findall(pattern, s):
    print(numbers, '*', letters)
```

```
''.join("%s * %s\n" % (n, w) for w, n in re.findall(r'(?i)([a-z]+)(\d+)', input_string))
```

the match, `m`, also has `start([<gidx>])` and `end([<gidx>])` which returns the start and end index of the string the match was found in the string.

[ref](https://stackoverflow.com/q/12870178/13041067)


## Regex syntax

- non-digits: `\D`
- non-capturing group: `(?:)`
    - this is particularly useful when you want a repetition of a pattern in a
      line to be captured as a whole, so you will do: `((?:somepattern)+)`. If
      you just do `(somepattern)+`, python will return the last matched string to
      `somepattern` in the repetition, and not the whole bunch of those strings.

Refs:

- [Python regex module](https://docs.python.org/3/library/re.html)
- [Python regex cheat-sheet](https://www.datacamp.com/cheat-sheet/regular-expresso)

