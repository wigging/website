---
title: Tuples in Rust
date: November 14, 2022
tags: rust
---

A tuple groups together values where each value can have a different type. Tuples have a fixed length and the first index is 0. In this example, a tuple is defined with three values of different types. The value is accessed using a period.

```rust
// Tuple with a variety of types
let tup: (i8, f64, u16) = (12, 4.05, 5);

// Access a tuple element using a period
let first_item = tup.0;

println!("First item is {first_item}");
// First item is 12
```

The values in a tuple can be extracted to separate variables as shown below.

```rust
// Extract tuple values to three separate variables
let tup = (12, 54, 102);
let (a, b, c) = tup;

println!("a is {a}, b is {b}, c is {c}");
// a is 12, b is 54, c is 102
```
