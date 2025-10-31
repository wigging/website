---
title: Arrays and Vectors in Rust
date: November 14, 2022
tags: rust
---

In Rust, arrays and vectors are both collections that store multiple elements of the same type. Arrays are fixed-size collections allocated on the stack. Vectors are dynamic arrays allocated on the heap that can grow and shrink at runtime.

## Arrays

An array is a collection of values where every element must have the same type. The length of an array is fixed and the first item is at index 0.

```rust
// Create an array of integers and access the first item
let a = [3, 4, 5, 6, 7, 8];
let first_item = a[0];

println!("First item in a is {first_item}");
// First item in a is 3
```

```rust
// Create an array with 3 elements of i64 and get the second item
let b: [i64; 3] = [12, 8, 5];
let second_item = b[1];

println!("Second item in b is {second_item}");
// Second item in b is 8
```

```rust
// Create an array of 4 elements where each element is 1
let c = [1; 4];

println!("The c array is {:?}", c);
// The c array is [1, 1, 1, 1]
```

```rust
// Get the length (number of elements) of an array
let d = [3, 4, 5, 6, 7];
let length_of_d = d.len();

println!("Length of d is {length_of_d}");
// Length of d is 5
```

## Vectors

A vector is a resizable collection that stores items of the same type. Its values are stored next to each other in memory. The `vec!` macro can be used to initialize a vector.

```rust
// Create a vector of numbers
let v1 = vec![3, 5, 8, 10, 12, 9];

// Create a vector of strings
let v2 = vec!["one", "two", "three"];
```

Below is an example of creating an empty vector and adding values to it.

```rust
// Add elements to an empty vector
let mut v3 = Vec::new();
v3.push(1.5);
v3.push(3.0);
v3.push(8.2);

println!("v3 is {:?}", v3);
// This prints:
// v3 is [1.5, 3.0, 8.2]
```

Use indexing to get values from a vector. Notice the first element is at index zero.

```rust
// Read elements from a vector
let v4 = vec![22, 38, 42, 50];
let first = &v4[0];
let third = v4[2];
let last = v4.last().unwrap();

println!("v4 is {:?}", v4);
println!("first is {}", first);
println!("third is {}", third);
println!("last is {}", last);
// This prints:
// v4 is [22, 38, 42, 50]
// first is 22
// third is 42
// last is 50
```

Use of `for` loop to iterate over the values in a vector.

```rust
// Iterate over elements in a vector
let v5 = vec![3, 4, 5, 6, 8, 12];

for v in v5 {
    println!("v in v5 is {}", v);
}
// This prints:
// v in v5 is 3
// v in v5 is 4
// v in v5 is 5
// v in v5 is 6
// v in v5 is 8
// v in v5 is 12

// Iterate over elements in a vector by reference
let v5 = vec![3, 4, 5, 6, 8, 12];

for v in &v5 {
    println!("v in v5 is {}", v);
}
// This prints the same as above.
```
