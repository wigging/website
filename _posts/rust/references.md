---
title: Rust References
date: November 14, 2022
tags: rust
---

A reference is denoted by an ampersand `&`. In the example below, a reference of the string `s1` is passed to the `calculate_length` function. The `&s1` refers to the value of `s1` without owning it.

```rust
fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(&s1);
    println!("The length of {s1} is {len}");
}

fn calculate_length(s: &String) -> usize {
    return s.len();
}
```

Running the above example generates the output shown below.

```
The length of hello is 5
```
