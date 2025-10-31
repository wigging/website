---
title: Compile and Run a Rust File
date: November 14, 2022
tags: rust
---

Below is the contents of a simple Rust program contained in a file named `sayhello.rs`.

```rust
// Contents of sayhello.rs that prints text to the screen.

fn main() {
    println!("Hello there");
}
```

To compile and run the file use the `rustc` command in the terminal.

```bash
# Compile a file
$ rustc sayhello.rs

# Run the compiled file to print text to the screen
$ ./sayhello
Hello there
```
