# Pairs That Sum

A Python function that finds every pair of integers in a list that adds up to a target value. It returns the results three ways: all pairs, unique ordered pairs, and unique number pairs.

## Example

```python
a = [1, 1, 2, 4, 4, 5, 5, 5, 6, 7, 9]
all_pairs, unique_pairs, unique_num_pairs = pairs_that_sum(a, 10)
```

| Output | Meaning | Result |
|---|---|---|
| `all_pairs` | Every index combination `(i, j)` with `i != j`, so duplicates and both orderings are kept | `[[1, 9], [1, 9], [4, 6], ...]` |
| `unique_pairs` | Duplicate pairs removed, but order still matters | `[[1, 9], [4, 6], [5, 5], [6, 4], [9, 1]]` |
| `unique_num_pairs` | Order ignored, so `[1, 9]` and `[9, 1]` count once | `[[1, 9], [4, 6], [5, 5]]` |

## How It Works

1. A nested loop compares every element against every other element, skipping an element paired with itself. Any pair whose sum equals the target is recorded.
2. Converting the pairs to tuples and putting them in a `set` removes exact duplicates.
3. Sorting each pair before deduplicating means `[9, 1]` and `[1, 9]` are treated as the same pair.
