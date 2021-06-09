def printsomething(counter):
    print("Start", counter)
    counter = counter+1
    if counter < 4:
        printsomething(counter)

        print("End", counter)


counter = 0
printsomething(counter)
