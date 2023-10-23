class Fibbo():
    def __init__(self , maximum_number=0 , num_of_iterations=0):
        self.max_num = maximum_number
        self.iter = num_of_iterations

    def __iter__(self):
        self.a = 0
        self.b = 1 
        self.counting = 0
        return self

    def __next__(self):
        if self.a <= self.max_num or self.counting < self.iter:
            self.aux = self.a
            self.a , self.b = self.b , self.a + self.b 
            self.counting += 1 
            # import pdb; pdb.set_trace()
            return f'sequence number {self.counting}  :   {self.aux}'
        else:
            raise StopIteration

prueba = Fibbo(num_of_iterations=500 )

for i in prueba:
    print(i)
