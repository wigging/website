---
title: Hash Maps in Rust
date: December 18, 2022
tags: rust
---

A hash map stores a key/value pair into memory. This is similar to a hash table or dictionary in other programming languages. The example below creates a new hash map, adds elements to it, then gets a value associated with a key.

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();
scores.insert("first", 10.5);
scores.insert("second", 34.09);

println!("scores are {:?}", scores);
println!("first score is {}", scores.get("first").copied().unwrap_or(0.0));
// Prints the following:
// scores are {"first": 10.5, "second": 34.09}
// first score is 10.5
```

Use a for-loop to iterate over the key/value pairs in the hash map.

```rust
use std::collections::HashMap;

let mut cars = HashMap::new();
cars.insert("ford", 1975);
cars.insert("chevy", 1988);
cars.insert("jeep", 1967);

for (key, value) in cars {
    println!("key is {key}, value is {value}");
}
// Prints the following:
// key is chevy, value is 1988
// key is ford, value is 1975
// key is jeep, value is 1967
```
