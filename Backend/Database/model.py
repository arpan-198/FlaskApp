#MODEL TO ENSURE DATA MODEL
class DataModel:
    def __init__(self):
        self.chk=True
        self.model={
            "name" : str,
            "img" : str,
            "summary" : str
        }
        self.keys=self.model.keys()
       
    def check(self,data):
        for dat in data:
            key=dat.keys()
            if len(key)==len(self.keys) and key == self.keys :
                for i in key:
                    if self.model[i] == type(dat[i]) :
                        continue
                    else :
                        self.chk=False
                        return self.chk
            else :
                self.chk=False
                break
        return self.chk
        
