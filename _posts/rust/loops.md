---
title: Rust Loops
date: November 14, 2022
tags: rust
---

Rust provides three kinds of loops: `loop`, `while`, and `for`. Use the `loop` keyword to execute code repeatedly until `break` is called.

```rust
let mut counter = 0;

let result = loop {
    counter += 1;

    if counter == 10 {
        let count = counter * 2;
        break count
    }
};

println!("The result is {result}");
// The result is 20
```

Use a `while` loop to run code while a condition is true.

```rust
let mut number = 3;

while number != 0 {
    println!("{number}...");

    number -= 1;
}

println!("Blast off!");
// 3...
// 2...
// 1...
// Blast off!
```

Use `for` to loop through each element in a collection.

```rust
let numbers = [10, 20, 30, 40, 50];

for n in numbers {
    println!("The number is: {n}");
}
// The number is: 10
// The number is: 20
// The number is: 30
// The number is: 40
// The number is: 50
```

Use `for` to execute some code for a certain number of times.

```rust
for i in 1..4 {
    println!("Number is {i}");
}
// Number is 1
// Number is 2
// Number is 3
```
