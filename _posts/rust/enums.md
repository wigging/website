---
title: Enums in Rust
date: January 30, 2023
tags: rust
---

An enum (or enumeration) represents data that is one of several possible variants. Each variant in the enum can optionally have data associated with it. An enumeration is declared using the `enum` keyword.

```rust
enum Fruit {
    Apple,
    Orange,
    Lemon,
    Mellon,
}

fn selection(fruit: Fruit) {
    match fruit {
        Fruit::Apple => println!("Selected the Apple fruit"),
        Fruit::Orange => println!("You chose the Orange fruit"),
        Fruit::Mellon => println!("You selected a Watermelon"),
        Fruit::Lemon => println!("Selected a Lemon fruit"),
    }
}

fn main() {
    let item1 = Fruit::Orange;
    selection(item1);

    let item2 = Fruit::Apple;
    selection(item2);

    let item3 = Fruit::Mellon;
    selection(item3);

    let item4 = Fruit::Lemon;
    selection(item4);
}
```

The output from the above example is shown below.

```
You chose the Orange fruit
Selected the Apple fruit
You selected a Watermelon
Selected a Lemon fruit
```
