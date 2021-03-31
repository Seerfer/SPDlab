def count_priority(times):
    tasks= list((map(list, zip(*times))))
    priorities_dict = {}
    index = 1
    for i in tasks:
        priorities_dict[index] = sum(i)
        index += 1
    priorities_dict = dict(sorted(priorities_dict.items(), key=lambda item: item[1], reverse=True))
    result = []

    max = True
    while list(priorities_dict.values()):
        print(priorities_dict)
        if max:
            choose = list(priorities_dict.keys())[0]
        else:
            choose = list(priorities_dict.keys())[-1]
        priorities_dict.pop(choose)
        max = not max