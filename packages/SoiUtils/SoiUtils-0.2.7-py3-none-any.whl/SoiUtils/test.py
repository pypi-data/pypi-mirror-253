from output_recorder import global_output_recorder

class test:
    def __init__(self,mul):
        self.mul = mul

    @global_output_recorder.record_output
    def __call__(self,a,b):
        return self.mul*(a+b)
    
    def update(self,new_mul):
        self.mul = new_mul

obj = test(4)
obj(5,3)
obj.update(5)
obj(6,3)
global_output_recorder.record_all = False
obj(7,3)

global_output_recorder.get_output()

