# toy
Toy for day.

## time string and timestamp convert

```python
python tt.py s2t "2017-09-10 12:45:50"

python tt.py t2s 1505018750
```

## find chinese string

```python
python fc.py find ./src --skipexts="jpg,jpeg,png,ico,svg" --onlyexts="html"
python fc.py find ./login.html --one true

python fc.py replace ./src --skipexts="jpg,jpeg,png,ico,svg" --onlyexts="html" --file out.json
python fc.py replace ./login.html --one true --file out.json
```