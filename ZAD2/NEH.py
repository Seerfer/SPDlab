def sum_of_list(l):
  total = 0
  for val in l:
    total = total + val
  return total

def count_priority(times):
    tasks= list((map(list, zip(*times))))
    priorities_dict = {}
    index = 1
    for i in tasks:
        priorities_dict[index] = sum(i)
        index += 1

    priorities_dict = dict(sorted(priorities_dict.items(), key=lambda item: item[1],  reverse = True))

    max =