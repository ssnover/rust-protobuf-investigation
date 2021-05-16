use std::io::Read;
use protobuf::Message;
use protobuf_example::TodoList::TodoList;

fn main() {
    let mut file = std::fs::File::open("./serialized.bin").unwrap();
    let mut serialized_todolist = Vec::new();
    file.read_to_end(&mut serialized_todolist).unwrap();

    let todolist = TodoList::parse_from_bytes(&serialized_todolist).unwrap();
    println!("{:?}", todolist);
}
