# Pickle RPC in Python
Very simple RPCs built with sockets & pickle in python. Support numpy as input and output arguments.

## Install
```bash
pip install picklerpc
```

## Example
Server
```python
import picklerpc
import numpy as np

# function
def numpy_create(shape, dtype):
    return np.arange(np.prod(shape), dtype=dtype).reshape(shape)

def hello():
    return "Hello, world!"

def hello2():
    return None

def add(a, b):
    return a+b

class HelloRPC(object):
    def hello3(self, name):
        return "Hello, %s" % name

# register
server = picklerpc.PickleRPCServer(('localhost', 9102))
server.register_function(numpy_create)
server.register_function(hello)
server.register_function(hello2)
server.register_function(lambda x,y: x-y, 'minus')
server.register_function(add)
server.register_instance(HelloRPC())  #from instance
server.serve_forever()
```

Client
```python
import picklerpc
import numpy as np

client = picklerpc.PickleRPCClient(('localhost', 9102))

print(client.numpy_create((3,4), dtype=np.float32))
print(client.hello())
print(client.hello3('From Instance'))
print(client.add(np.range(10), 3))
print(client.minus(np.range(10), 3))
```

## Speed compare

The picklerpc is most 10x faster than `zerorpc` and `xmlrpc`.

|                    | zerorpc | xmlrpc  | picklerpc (mine)    |
| ------------------ | ------- | ------- | ------------------- |
| Protocal           | tcp     | http    | tcp                 |
| Data Stream        | -       | xml     | pickle              |
| Multiple Client    | Yes     | Yes     | Yes                 |
| Data Types         | Natives | Natives | Natives + **Numpy** |
| Speed (local loop) | 683 µs  | 462 µs  | 59 µs               |
| Speed (remote)     | 2.76 ms | 4.64 ms | 0.54 ms             |





## Reference

> Thanks https://github.com/TarasZhere/RPC