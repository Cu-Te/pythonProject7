from student import Student


def main():
    st1 = Student("alex", 20, 10)
    st2 = Student()

    # st1.init("alex", 20, 10)
    # st1.name = "Alex"
    # setattr(st1, "name", "Piter")
    # st1.__setattr__("name","Olya")

    # st2.name = "Anna"
    # st1.mark = 10
    # st2.mark = 7
    # st1.age = 20
    # st2.age = 17

    # print(st1.name)
    # print(getattr(st1, "name"))

    # del st1.name
    # delattr(st1, "mark")
    # st1.__delattr__("age")

    print(vars(st1))
    print(vars(st2))

    # print(st1.__dict__)


if __name__ == '__main__':
    main()
