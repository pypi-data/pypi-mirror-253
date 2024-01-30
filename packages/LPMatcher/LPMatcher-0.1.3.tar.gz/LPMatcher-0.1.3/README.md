# Points and lines matcher

## This module is baesd on  hungarian match with cost  matrix

## Example:

```python
from  LPMatcher import topology_match

xmin, ymin, xmax, ymax = [97, 348, 533, 620], [131, 133, 180, 50], [197, 451, 581, 660], [186, 209, 281, 120]
test_points = list(zip(xmin, ymin, xmax, ymax))
test_lines = [((638, 2), (638, 47)),((455, 159), (638, 159)), ((638, 124), (638, 159)), ((639, 159), (713, 159)), ((3, 159), (93, 159)),
              ((201, 159), (344, 159)), ((557, 161), (557, 176))]
tm = topology_match(img_path='./img/test2.png', lines=test_lines, points=test_points)
print("the number of lines: " ,tm.get_line_num)
print("the number of points: ", tm.get_point_num)
match_map = tm.hungarian_match_with_cost(distance_threshold=60, show=False)
print(match_map)
```
