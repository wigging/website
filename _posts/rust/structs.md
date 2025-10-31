---
title: Structs in Rust
date: November 14, 2022
tags: rust
---

A `struct` is a custom data type that contains related values. Below are some examples of creating structs and accessing its values.

## A basic struct

A basic example of defining a struct and accessing its values is given below.

```rust
// A basic struct

struct Point {
    x: i32,
    y: i32
}

fn main() {

    // Using a basic struct

    let p = Point {
        x: 13,
        y: 8
    };

    println!("x is {}, y is {}", p.x, p.y);
}
```

Output from the above example.

```
x is 13, y is 8
```

## Tuple structs

Here is an example of a tuple struct.

```rust
// A tuple struct

struct PointTuple(i32, i32);

fn main() {

    // Using a tuple struct

    let pt = PointTuple(32, 16);

    println!("x is {}, y is {}", pt.0, pt.1);
}
```

```
x is 32, y is 16
```

## Methods

And here is an example of defining methods associated with a struct.

```rust
// A struct with methods (functions)

struct Shape {
    width: u32,
    height: u32
}

impl Shape {

    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn volume(&self, v: u32) -> u32 {
        self.width * self.height * v
    }
}

fn main() {

    // Using a struct with methods

    let shape = Shape { width: 2, height: 3 };
    let area = shape.area();
    let volume = shape.volume(2);

    println!("Area is: {area}");
    println!("Volume is: {volume}");
}
```

```
Area is: 6
Volume is: 12
```
