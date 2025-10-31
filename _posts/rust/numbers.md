---
title: Numbers in Rust
date: November 14, 2022
tags: rust
---

Signed integer types are `i8` (8-bit), `i16` (16-bit), `i32` (32-bit), `i64` (64-bit), and `i128` (128-bit). The default integer type is i32. Numbers represented by signed integers can have a positive or negative value.

```rust
// Examples of signed integers
let a: i8 = -23;
let b: i32 = -41;
let c: i64 = -52;
```

Unsigned integer types are `u8` (8-bit), `u16` (16-bit), `u32` (32-bit), `u64` (64-bit), and `u128` (128-bit). Numbers represented as unsigned integers must have a positive value.

```rust
// Examples of unsigned integers
let a: u8 = 58;
let b: u32 = 81;
let c: u64 = 95;
```

Floating point number types are `f32` (single precision) and `f64` (double precision). The default float type is `f64`.

```rust
// Examples of floating point numbers
let a: f32 = 12.809;
let b = 34.1;
```

Use an underscore to visually separate a number.

```rust
let c = 9_800.25;
```