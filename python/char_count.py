def char_count(string):
  char_dict = {}
  clean_str = ''.join(c for c in string if c.isalnum()).lower() # remove all spaces, punc and lower case

  for char in clean_str:
    if char in char_dict:
      char_dict[char] += 1
    else:
      char_dict[char] = 1 # loop thru and count # of characters- set to 1 if one occurence and add up if more than 1

  sorted_count = sorted(char_dict.items(), key =lambda x: (-x[1], x[0])) # list that is sorted by descending count (-x[1])and alphabetically (x[0])

  result = [[char, count] for char, count in sorted_count] # convert to list of lists

  return result