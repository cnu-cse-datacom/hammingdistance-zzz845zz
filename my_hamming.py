import random
import numpy as np
import pandas as pd

df = pd.read_csv("sample.csv", names=['word', 'bin'])

def generate_random_ascii():
    for i in range(0, 100):
        make_str = list()
        make_ascii = list()
        make_hex = list()
        for j in range(0, 4):
            num = random.randint(97, 122)  # 'a'~'z'
            make_str.append(str(chr(num))) # 97을 문자 'a'로 추가
        string = ''.join(make_str)
        binary = bin(int.from_bytes(string.encode(), 'big')) # binary
    return string, binary

def hamming(a, b):
    #print(list(zip(a, b)))
    #print([i for i in filter(lambda x: x[0]!=x[1], zip(a, b))])
    return len([i for i in filter(lambda x: x[0]!=x[1], zip(a, b))])


def main():
    # sample.csv 랜덤 생성
    for k in range(0, 100):
        string, binary = generate_random_ascii()
        df.iloc[k, 0] = string # 문자 추가
        df.iloc[k, 1] = "0"+binary[2:] # 2진수 추가
    df.to_csv("sample.csv", header=False, index=False)

    min_value = 100000000000
    size = int(df.size)//2
    count = 1
    for i in range(df.__len__()):
        for j in range(i+1, size):
            hd = hamming(df.iloc[i, 1], df.iloc[j, 1])
            min_value = min(min_value, hd)
            print(count, "(", df.iloc[i, 0], df.iloc[j, 0],")", "hamming_distance", hd )
            count = count+1
    print(min_value)

main()