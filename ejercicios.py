my_list = [1,2,3,4,5]
def gen_list_transformer(transformacion):
    def transformer(element):
        return [transformacion(i) for i in element]
    return transformer

square_of_list = gen_list_transformer(lambda x: x ** 2)
cube_of_list = gen_list_transformer(lambda x: x ** 3)
