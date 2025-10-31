---
title: FizzBuzz in Rust
date: December 11, 2022
tags: rust
---

Examples of the classic fizzbuzz problem are implemented below. The first example uses if-else statements while the second example uses pattern matching.

```rust
fn main() {

    // Example 1

    for i in 1..21 {
        print!("i is {} ", i);
        if i % 5 == 0 && i % 3 == 0 {
            println!("FizzBuzz");
        } else if i % 5 == 0 {
            println!("Fizz");
        } else if i % 3 == 0 {
            println!("Buzz");
        } else {
            println!("");
        }
    }

    // Example 2

    for i in 1..21 {
        print!("i is {} ", i);
        match (i % 3, i % 5) {
            (0, 0) => println!("FizzBuzz"),
            (_, 0) => println!("Fizz"),
            (0, _) => println!("Buzz"),
            _ => println!(""),
        }
    }

}
```

Each of the above examples will print the same output. This output is shown below.

```
i is 1
i is 2
i is 3 Buzz
i is 4
i is 5 Fizz
i is 6 Buzz
i is 7
i is 8
i is 9 Buzz
i is 10 Fizz
i is 11
i is 12 Buzz
i is 13
i is 14
i is 15 FizzBuzz
i is 16
i is 17
i is 18 Buzz
i is 19
i is 20 Fizz
```
