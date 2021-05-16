# Explanation
Two components here: a python3 script which generates a TodoList object, serializes it, and writes it to file `serialized.bin` and a Rust program which reads `serialized.bin`, deserializes it, and prints it.

The protobuf files were generated using protocol buffers version 3.14 with the following commands:
* `protoc --python_out=. ./TodoList.proto`
* `protoc --rust_out . TodoList.proto`

In particular, the Rust code is generated with a plugin for `protoc` that can be installed with `cargo install protobuf-codegen` as documented here: https://github.com/stepancheg/rust-protobuf/tree/master/protobuf-codegen. The resulting binary must be in the path for `protoc` to find it.

# References
* https://www.freecodecamp.org/news/googles-protocol-buffers-in-python/
* https://developers.google.com/protocol-buffers/docs/pythontutorial
* https://github.com/stepancheg/rust-protobuf
* https://github.com/stepancheg/rust-protobuf/blob/master/protobuf-examples/src/main.rs