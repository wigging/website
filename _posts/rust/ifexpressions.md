---
title: If Expressions in Rust
date: November 14, 2022
tags: rust
---

Use an `if` expression to check if a condition is met or not met. The `else` expression is used to check for multiple conditions.

```rust
fn main() {

    let item = 3.5;

    // Basic `if` expression
    if item == 3.5 {
        println!("Item is 3.5");
    }

    // A simple if-else expression
    if item < 3.0 {
        println!("Less than 3");
    } else {
        println!("Greater than 3");
    }

    // Check multiple conditions
    if item / 3.0 == 0.0 {
        println!("Item is divisible by 3");
    } else if item < 3.0 {
        println!("Less than 3");
    } else {
        println!("Item not divisible by 3 or less than 3");
    }

    // Use `if` in a `let` statement
    let high = true;
    let condition = if high { "yes" } else { "no" };
    println!("Are you high: {condition}");
}
```
