import TodoList_pb2 as TodoList

my_list = TodoList.TodoList()
my_list.owner_id = 1234
my_list.owner_name = "Tim"

first_item = my_list.todos.add()
first_item.state = TodoList.TASK_DONE
first_item.task = "Test ProtoBuf for Python"
first_item.due_date = "31.10.2019"

print(my_list)
print(my_list.SerializeToString())

with open("./serialized.bin", "wb") as fd:
    fd.write(my_list.SerializeToString())