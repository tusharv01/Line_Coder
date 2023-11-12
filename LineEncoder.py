import matplotlib.pyplot as plt
import numpy as np
import random

def encode_decode_and_plot(ch, input_data):
    result = line_encoder(ch, input_data)
    print(f"Encoded Data for Scheme {ch}")
    print(result)

    decode_choice = input("Do you want to decode the signal? (yes/no): ")
    if decode_choice.lower() == "yes":
        decoded_data = line_decoder(ch, result)
        print(f"Decoded Data for Scheme {ch}")
        print(decoded_data)

    draw(result, len(result), f"Scheme {ch}")


def randSeq(length, probability):
    random.seed(0)
    val = []

    if probability == 1:
        lst = [1, 0]
        for _ in range(0, length):
            val.append(random.choice(lst))
    elif probability == 2:
        lst = [1, 0, 0, 0]
        for _ in range(0, length):
            val.append(random.choice(lst))
    elif probability == 3:
        lst = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        for _ in range(0, length):
            val.append(random.choice(lst))
    return val


def polar_nrz_l(inp):
    return [-1 if i == 0 else 1 for i in inp]


def polar_nrz_i(inp):
    inp2 = list(inp)
    flag = False

    for i in range(len(inp2)):
        if inp2[i] == 1 and not flag:
            flag = True
            continue
        if flag and inp2[i] == 1:
            if inp2[i - 1] == 0:
                inp2[i] = 1
                continue
            else:
                inp2[i] = 0
                continue
        if flag:
            inp2[i] = inp2[i - 1]

    return [-1 if i == 0 else 1 for i in inp2]


def manches(inp):
    inp1 = list(inp)
    manches = []
    for i in inp1:
        if i == 1:
            manches.append(-1)
            manches.append(1)
        else:
            manches.append(1)
            manches.append(-1)
    return manches


def polar_rz(inp):
    inp1 = list(inp)
    inp1 = [-1 if i == 0 else 1 for i in inp1]
    li = []
    for i in range(len(inp1)):
        li.append(inp1[i])
        li.append(0)
    return li


def AMI(inp):
    inp1 = list(inp)
    flag = False
    for i in range(len(inp1)):
        if inp1[i] == 1 and not flag:
            flag = True
            continue
        elif flag and inp1[i] == 1:
            inp1[i] = -1
            flag = False
    return inp1


def B8ZS(inpt):
    inp = inpt[0:]
    r = []
    prev = 1
    count = 0
    for i in range(len(inp)):
        if inp[i] == 0:
            count = 1
            for j in range(1, 8):
                if i + j < len(inp):
                    if inp[i + j] == 0:
                        count += 1
                    else:
                        break
                else:
                    break
            if count == 8:
                for j in range(1, 8):
                    inp[i + j] = -1
                r.append(0)
                r.append(0)
                r.append(0)
                r.append(prev)
                prev = prev * -1
                r.append(prev)
                r.append(0)
                r.append(prev)
                prev = prev * -1
                r.append(prev)
                count = 0
            else:
                r.append(inp[i])
        elif inp[i] == 1:
            prev = inp[i]
            r.append(inp[i])
        else:
            continue
    return r


def count_nonzero_pulses(l):
    count = 0
    for i in range(len(l)):
        if l[i] == 1 or l[i] == -1:
            count = count + 1
    return count


def Diff_manchester(inp):
    li = []
    if inp[0] == 1:
        li.append(-1)
        li.append(1)
    else:
        li.append(1)
        li.append(-1)
    for i in range(1, len(inp[1:])):
        if li[-1] == 1:
            if inp[i] == 1:
                li.append(-1)
                li.append(1)
            else:
                li.append(1)
                li.append(-1)
        else:
            if inp[i] == 1:
                li.append(1)
                li.append(-1)
            else:
                li.append(-1)
                li.append(1)
    return li


def hdb3(inpt):
    inp = inpt[0:]
    r = []
    prev = 1
    count = 0
    parity = 0
    for i in range(len(inp)):
        if inp[i] == 0:
            count = 1
            for j in range(1, 4):
                if i + j < len(inp):
                    if inp[i + j] == 0:
                        count += 1
                    else:
                        break
                else:
                    break
            if count == 4:
                for j in range(1, 4):
                    inp[i + j] = -1
                if parity % 2 == 1:
                    r.append(0)
                    r.append(0)
                    r.append(0)
                    r.append(prev)
                    parity += 1
                else:
                    prev = prev * -1
                    r.append(prev)
                    r.append(0)
                    r.append(0)
                    r.append(prev)
                count = 0
            else:
                r.append(inp[i])
        elif inp[i] == 1:
            parity += 1
            prev = inp[i]
            r.append(inp[i])
        else:
            continue
    return r


def lps(inp):
    inp = list(map(str, inp))
    inpt = ""
    for x in inp:
        inpt += x
    reverse = inpt[::-1]
    lookup = [[0 for x in range(len(inpt) + 1)] for y in range(len(inpt) + 1)]
    print('The length of the longest palindromic subsequence is',
          LCSLength(inpt, reverse, len(inpt), lookup))
    print('The longest palindromic subsequence is',
          findLongestPalindrome(inpt, reverse, len(inpt), len(reverse), lookup))


def draw(result, bit, data):
    if bit == 2:
        if data == "Original":
            x = np.arange(0, len(result) + 1)
            plt.xlim(0, len(result))
            plt.ylim(-1.5, 2)
            plt.ylabel('Value')
            plt.title(data)
            array = result
            for i in range(len(result)):
                plt.text(i + 0.4, 1.5, array[i])
            plt.style.use('seaborn-dark')
            plt.grid(1)
            plt.xticks(x)
            plt.step(x, [array[0]] + array)
            plt.gcf().set_size_inches(24, 6)
            plt.show()
        else:
            x = np.arange(0, len(result) + 1)
            plt.xlim(0, len(result))
            plt.ylim(-2, 2)
            plt.ylabel('Value')
            plt.title(data)
            array = result
            for i in range(len(result)):
                plt.text(i + 0.4, 1.5, array[i])
            plt.style.use('seaborn-dark')
            plt.grid(1)
            plt.xticks(x)
            plt.step(x, [array[0]] + array)
            plt.gcf().set_size_inches(24, 6)
            plt.show()
    elif bit == 3:
        x = np.arange(0, len(result) + 1)
        plt.xlim(0, len(result))
        plt.ylim(-2, 2)
        plt.ylabel('Value')
        plt.title(data)
        array = result
        for i in range(len(result)):
            plt.text(i + 0.4, 1.5, array[i])
        plt.style.use('seaborn-dark')
        plt.grid(1)
        plt.xticks(x)
        plt.step(x, [array[0]] + array)
        plt.gcf().set_size_inches(24, 6)
        plt.show()


def pcm_encoder(inp):
    # Your PCM encoding logic here
    return inp


def delta_modulation(inp):
    # Your Delta Modulation encoding logic here
    return inp


def line_decoder(ch, result):
    # Your decoding logic for each scheme here
    if ch == 1:
        return result
    elif ch == 2:
        return result
    elif ch == 3:
        return result
    elif ch == 4:
        return result
    elif ch == 5:
        return result
    elif ch == 6:
        return result
    elif ch == 7:
        return result
    elif ch == 8:
        return result
    elif ch == 9:
        return pcm_encoder(result)  # PCM decoding
    elif ch == 10:
        return delta_modulation(result)  # Delta Modulation decoding
    else:
        return result


def line_encoder(ch, input_data):
    # Your common encoding logic here
    if ch == 9:
        return pcm_encoder(input_data)  # PCM encoding
    elif ch == 10:
        return delta_modulation(input_data)  # Delta Modulation encoding
    elif ch == 1:
        return polar_nrz_l(input_data)
    elif ch == 2:
        return polar_nrz_i(input_data)
    elif ch == 3:
        return manches(input_data)
    elif ch == 4:
        return polar_rz(input_data)
    elif ch == 5:
        return AMI(input_data)
    elif ch == 6:
        return B8ZS(input_data)
    elif ch == 7:
        return Diff_manchester(input_data)
    elif ch == 8:
        return hdb3(input_data)


if __name__ == '__main__':
    print("Welcome to Tushar Verma's Line Encoder")
    print("Choose the following\n 1:Initialize Random Input\n 2:Enter Custom Input")

    choice = int(input())

    if choice == 1:
        length = int(input("Enter Length of Random input\n"))
        probability = int(input("Choose Ratio Of 0:1\n 1-50:50\n 2-75:25\n 3-85:15\n"))
        input_data = randSeq(length, probability)
        print("Random Input Data")
        print(input_data)
    elif choice == 2:
        data = input("Enter your Custom Input In NRZ Format\n")
        input_data = [int(bit) for bit in data]
        print("Input Data")
        print(input_data)

    lps(input_data)

    while True:
        choice = int(input(
            "Choose the following\n\t1:Polar NRZ-L\n\t2:Polar NRZ-I\n\t3:Manchester\n\t4:Polar RZ\n\t5:AMI\n\t6:Scrambling AMI B8ZS(Bipolar with 8 zero substitution)\n\t7:Differential Manchester\n\t8:Scrambling AMI HBD3(High-Density Bipolar 3 Zeros)\n\t9:PCM\n\t10:Delta Modulation\n\t11:Exit\n\t "))

        if choice == 11:
            break

        encode_decode_and_plot(choice, input_data)

    print("Good Bye and Keep Smiling. . . .")
    print("\U0001F44B")
