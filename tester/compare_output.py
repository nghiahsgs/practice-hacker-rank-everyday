import io

def readfile(filename):
    f=io.open(filename, 'r',encoding='utf-8')
    ndung=f.read()
    f.close()
    return ndung


expected_output=readfile('expected output')
my_output=readfile('my output')

expected_list=expected_output.split('\n')
my_lilst=my_output.split('\n')
input_list=readfile('input').split('\n')

for index, expected_value in enumerate(expected_list):
    my_value=my_lilst[index]
    input_value=input_list[index]
    if my_value != expected_value:
        print('--error--')
        print('input:',input_value)
        print('my output:',my_value)
        print('expected output:',expected_value)





