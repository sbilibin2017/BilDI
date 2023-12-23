# BilDI

### description:
mini dependency injection framework working with type annotations

### usage

```
from typing import Protocol

class IRepository(Protocol):
    def say_hello(self) -> str:
        ...
        
class Repository1:
    def say_hello(self) -> str:
        return "hello from repository1"
    
class Repository2:
    def say_hello(self) -> str:
        return "hello from repository2"
    
class IService(Protocol):
    @property
    def repository1(self) -> IRepository:
        ...
        
    @repository1.setter
    def repository1(self) -> IRepository:
        ...
        
    @property
    def repository2(self) -> IRepository:
        ...
        
    @repository2.setter
    def repository2(self) -> IRepository:
        ...
        
    def say_hello(self):
        ...
        
        
class Service:
    def __init__(self, repository1: IRepository, repository2: IRepository):
        self.repository1=repository1
        self.repository2=repository2
    
    def say_hello(self):
        h1 = self.repository1.say_hello()
        h2 = self.repository2.say_hello()
        return f"{h1}, {h2}"

# init container
di_container = BilDI()

# register members
di_container.register("repository1", IRepository, Repository1)
di_container.register("repository2", IRepository, Repository2)
di_container.register("service", IService, Service)

# resolve service and sat hello
di_container.resolve("service").say_hello()
>> hello from repository1, hello from repository2
```

### TODO
- [ ] add tests
- [ ] add makefile
- [ ] add ci workflow


