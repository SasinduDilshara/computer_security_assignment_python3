import pickle

class FileReader:

    @staticmethod
    def loadall(filename):
        '''
        loadall(filename)
        This method return all the data conatined in that file
        '''
        with open(filename, "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
    @staticmethod
    def add(filename,obj):
        '''
        add(filename,object)
        This method add new detail
        '''
        with open(filename, "ab") as f:
            try:
                pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
                return True
            except Exception as e:
                print("Error occur when writing to file")
                print(e)
                return False
    
            
