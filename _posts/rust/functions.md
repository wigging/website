---
title: Rust Functions
date: November 14, 2022
tags: rust
---

Functions in Rust are defined with `fn`. The function name and its input arguments should be lowercase with underscores to separate words. Some examples of functions are shown below.

```rust
fn main() {

    basic_function();

    let sum = adder(2, 3);
    println!("The sum is {sum}");

    let frac = divider(5.0, 2.0);
    println!("The fraction is {frac}");
}

// A basic function with no inputs

fn basic_function() {
    println!("Basic function with no inputs");
}

// Use the return keyword to return a value

fn adder(x: i32, y: i32) -> i32 {
    let s = x + y;
    return s
}

// This function uses an expression to return its value. Notice the absence of
// a semicolon after the expression in the function.

fn divider(x: f32, y: f32) -> f32 {
    x / y
}
```
