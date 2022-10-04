from datetime import date
# difference between dates
today = date.today()
start_date = date(2021,6,19)
difference = abs(today-start_date).days
with open('word_list.txt') as f:
    words = f.readlines()
words = words[0].replace('"', '').split(",")
print("today's wordle:")
print(words[difference])

while True:
    more_days = input("do you want more days wordles")
    if ( more_days == "yes" ):
        num_more_days = input("how many days  later")
        try:
            num_more_days = int(num_more_days)
            print("the wordle in " + str(num_more_days) + " days is:")
            print(words[difference + num_more_days])
        except:
            if ( num_more_days == "break" ):
                break
            else:
                print("give me a number you stupid idot")
    else:
        break