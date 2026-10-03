---
date: November 7, 2022
description: Assign values in a NumPy array based on a boolean condition.
tags: python, numpy
---

## Boolean Indexing with NumPy

Use boolean indexing in NumPy arrays to assign values. The example below assigns a zero to array items that are less than zero.

```python
import numpy as np

nums = np.array([-1, 3, 6, -0.2, -4])
nums[nums < 0] = 0

print(nums)
# array([0., 3., 6., 0., 0.])
```
