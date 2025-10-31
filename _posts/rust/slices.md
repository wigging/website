---
title: Slices in Rust
date: November 14, 2022
tags: rust
---

A slice is a reference to a sequence of elements in a collection such as a string or array. In this example, the `s` string is sliced to obtain a reference of the first word and second word in the string.

```rust
let s = String::from("hello there");
let firstword = &s[0..5];
let secondword = &s[6..11];
println!("phrase is: {s}");
println!("first word is: {firstword}");
println!("second word is: {secondword}");
```

The above example prints the following:

```
phrase is: hello there
first word is: hello
second word is: there
```

The range syntax can omit the first index when starting at index zero. It can also omit the last index if the last item is included in the range.

```rust
let firstword = &s[..5];
let secondword = &s[6..];
println!("first word is: {firstword}");
println!("second word is: {secondword}\n");
```

This prints the same output as the previous example:

```
first word is: hello
second word is: there
```

Slices can be applied to arrays as shown below.

```rust
let items = [1, 2, 3, 4, 5];
let slice = &items[1..4];
println!("items are: {:?}", items);
println!("items slice is: {:?}", slice);
```

```
items are: [1, 2, 3, 4, 5]
items slice is: [2, 3, 4]
```
