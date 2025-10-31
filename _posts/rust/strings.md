---
title: Strings in Rust
date: December 18, 2022
tags: rust
---

A string literal uses double quotes `" "` and represents a string slice `str` or `&str`.

```rust
// String literal which is a string slice str or &str
let s1 = "hello there";

// String literal with emoji smiley face
let s2 = "hello there 😀";
```

Loop through the characters in a string.

```rust
let s3 = "hello";

for c in s3.chars() {
    println!("char is {c}");
}

// Prints the following:
// char is h
// char is e
// char is l
// char is l
// char is o
```

Get the second character in a string.

```rust
let s4 = "strawberry";
println!("second char is {}", s4.chars().nth(1).unwrap());

// Prints the following:
// second char is t
```

Create a `String` type from a string literal.

```rust
let s5 = String::from("hello again");
```

Create an empty `String` type and append to it.

```rust
let mut s6 = String::new();
s6.push_str("one");
s6.push_str("two");

println!("s6 is {s6}");

// Prints the following:
// s6 is onetwo
```

Use the `format!` macro to combine strings.

```rust
let a = String::from("tic");
let b = String::from("tac");
let c = String::from("toe");

let s = format!("{a}-{b}-{c}");

println!("s is {s}");

// Prints the following:
// s is tic-tac-toe
```
