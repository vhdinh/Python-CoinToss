import random
counthead = 0
counttail = 0

for i in range(1,5001):
    random_num = random.random()

    if random_num < 0.5:
        counthead = counthead + 1
        print "attempt #%s; Thowing a coin... It's a head!... got %s head(s) so far and %s tails(s) so far" %(i, counthead, counttail)
    else:
        counttail = counttail + 1
        print "attempt #%s; Thowing a coin... It's a tail!... got %s head(s) so far and %s tails(s) so far" %(i, counttail, counthead)
print "Ending the program, thank you!"
