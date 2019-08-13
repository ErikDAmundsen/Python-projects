inp = input('Enter your IP address')
count = 0
segments = 1
if len(inp)>0:

    for char in inp:
        if char != '.':
            count += 1
        elif char=='.':
            print("Segment {0} contains {1} characters".format(segments,count))
            segments +=1
            count =0
    print("Segment {0} contains {1} characters".format(segments,count) )
else:
    print("please enter a valid answer")