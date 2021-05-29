import ipaddress

def correct_malformed_date(val):
    txt = str(val)
    txt_split = txt.split(":")
    hour = int(txt_split[0]) * 3600
    minute = int(txt_split[1]) * 60
    second = int(txt_split[2])
    total_seconds = hour + minute + second
    correct_hour = int(total_seconds/3600)
    correct_minute = int((total_seconds-(correct_hour*3600))/60)
    correct_second = int(total_seconds - correct_minute*60) % 60
    semi_colon = ":"
    zero = "0"
    if correct_second < 10:
        print(str(correct_hour) + semi_colon + str(correct_minute) + semi_colon+zero + str(correct_second))
        return (str(correct_hour) + semi_colon + str(correct_minute) + semi_colon+zero + str(correct_second))
    else:
        print(str(correct_hour) + semi_colon + str(correct_minute) + semi_colon + str(correct_second))
        return (str(correct_hour) + semi_colon + str(correct_minute) + semi_colon + str(correct_second))

def convert_int_to_ip(val):
    addr = ipaddress.ip_address(val)
    print(addr)
    return addr

def convert_ip_to_int(str):
    addr = ipaddress.ip_address(str)
    addr1 = int(addr)
    print(addr1)
    return addr1

def is_isogram(word):
    clean_word = word.lower()
    letter_list = []
    for letter in clean_word:
       if letter.isalpha():
            if letter in letter_list:
                print('False')
                return False
            letter_list.append(letter)
    print('True')
    return True

def mexicanwave(s):
    #s='hello'
    new=[]
    for i, val in enumerate(s[:]):
        up=s[i].upper()
        c=s[:i] + up + s[i+1:]
        new.append(c)
    print(new)
    return new

def maxnumber(n, k):
    for i in range(0, k):
        ans = 0
        i = 1
        while n // i > 0:
            temp = (n//(i * 10))*i + (n % i)
            i *= 10
            if temp > ans:
                ans = temp
            n = ans       
    print(ans)
    return ans

def maximumsuffle(num):    
    count = [0 for x in range(10)]   
    string = str(num)
    for i in range(len(string)):
        count[int(string[i])] = count[int(string[i])] +  1
    result = 0
    multiplier = 1    
    for i in range(10):
        while count[i] > 0:
            result = result + ( i * multiplier )
            count[i] = count[i] - 1
            multiplier = multiplier * 10
    print(result)
    return result

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    print(counts)
    return counts
 
def rgb_to_hex(rgb):
    print('%02x%02x%02x' % rgb)
    return '%02x%02x%02x' % rgb


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    print(tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3)))
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))


correct_malformed_date('5:70:65')
convert_int_to_ip(42540766400282592856903984001653826561)
convert_ip_to_int('2001:db7:dc75:365:220a:7c84:d796:6401')
is_isogram('elephant')
maxnumber(6385,1)
rgb_to_hex((255, 255, 195))
hex_to_rgb("FF65BA")
mexicanwave('hello')
maximumsuffle(1998)
word_count('I am am a boy')