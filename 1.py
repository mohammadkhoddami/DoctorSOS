class Mmd:
    def __init__(self):
        self.mmd = 'mmd'
        self.age = 24
        self.koft = 'zahrmar'
    
    @property
    def koft_va_zhrmr(self):
        return f'{self.koft} Vaaaaaaaaaaa KOOOOOOOOOFT'
    
mmd = Mmd()


print(mmd.koft_va_zhrmr)