class A:
    def __init__(self) -> None:
        self.a = 1
    def __str__(self) -> str:
        return f'A with {self.a}'
    
i = A()

print(i)