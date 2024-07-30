def modified_generator():
    while True:
        value = (yield)
        if value is None:
            break
        print(value)

gen = modified_generator()
next(gen)         
gen.send(10)       
gen.send(20)       
gen.close()
