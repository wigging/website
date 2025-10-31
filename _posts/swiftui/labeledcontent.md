---
title: LabeledContent in SwiftUI
date: November 13, 2022
tags: swiftui
---

The LabeledContent view is comprised of a label and content. Usually, it displays the label on the leading edge and the content on the trailing edge. This is similar to using an HStack containing two views.

<p><img src="../../assets/images/swiftui-labeledcontent.png" style="max-width:300px;" alt="labeled content"></p>

```swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack {
            Text("Below are labeled content examples.")

            LabeledContent("Favorites") {
                Image(systemName: "star.fill")
            }

            LabeledContent("Wireless") {
                Image(systemName: "wifi")
            }
        }
        .frame(width: 300, height: 200)
    }
}
```
