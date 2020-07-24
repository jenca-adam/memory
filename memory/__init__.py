
import os,pickle


class Memory:
    def __init__(self,**kwargs):
        self.list=[]
        self.infile=False
        self.file=None
        if 'infile' in kwargs.keys():
            if kwargs['infile'] is True:
                if 'file' not in kwargs.keys():
                    raise ValueError('If you specify a "infile" argument as True, you must specify a "file"argument')
                else:
                    self.infile=True
                    self.filename=kwargs['file']
                if os.path.exists(os.path.expandvars(os.path.join(os.curdir,kwargs['file']))):

                    self.file=open(kwargs['file'],'rb')
                    try:
                        self.list=pickle.load(self.file)
                    except EOFError:pass
                    self.file.close()
                    self.file=open(kwargs['file'],'wb')
                else:
                    self.file=open(kwargs['file'],'wb')
            else:
                self.infile=False
    def __getitem__(self,index):
        return self.list[index]
    def __setitem__(self,index,towhat):
        self.list[index]=towhat
    def printitems(self):
        print(*self.list,sep='\n')
    def __del__(self):
        if self.infile:
            self.save()
            self.end()
            self.clear()
    def feed(self,*args):
        self.list.extend(args)
    def clear(self):
        self.list=[]
    def save(self):
        if not self.infile:
            raise BaseException('You cannot save the memory if you have not any file')
        pickle.dump(self.list,self.file)
    def end(self):
        if not self.infile:
            raise BaseException('You cannot end if you have not saved memory in file')
        if not self.file.closed:
            self.file.close()
        else:
            raise IOError('You cannot end if the file is closed')
    def reopen(self):
        self.file=open(self.filename,'wb')




    
     




