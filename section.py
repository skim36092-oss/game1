class Section:
    __max_person=0


    def __init__(self, name: str,graphic: dict):

          self. __name = name
          self.__graphic= graphic


    def  __str__(self):
        return f"название: {self.__name}| график: {"нет" if len(self.__graphic.keys()) ==  0 else self.graphic}| людей в секции:{self.__max_person}"


    @property
    def name(self):
        return self.__name


    @property
    def graphic(self):
        return self.__graphic



    def add_person(self):
        self.__max_person +=1



if __name__ =='__main__':
    section1=Section('А',{'1':'2'})
    print(section1)