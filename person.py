class Person:
    __sections = set()
    def __init__(self,fio,phone):
        self.__fio = fio
        self.__phone = phone





    def __str__(self):
       return f'фио: {self.__fio}| номер телефона:{self.__phone}| секции {"нет" if len(self.__sections) == 0 else self.__sections}'

    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio:str):
        self.__fio=fio

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    def add_section(self,name):
        self.__sections.add(name)


if __name__=='__main__':
    person1=Person( 'fio',' 9859473')
    person1.add_section('1')
    print(person1)
    person1.add_section('2')
    print(person1)
