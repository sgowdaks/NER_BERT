from operator import itemgetter
from argparse import ArgumentParser

accept_labels = {'B-Element', 'B-Mineral', 'B-Target', 'Element', 'Mineral', 'Target'}


def converter(p):
    #opens each file and converts it into a list
    with open(p) as f:
        lines = f.readlines()
    if lines == []:
        return
    nums = []
    k = []
    for i in lines:
      # print(i)
      l = i.split("\t")
      print(l)
      m = l[1].split(" ")
      if m[0] not in accept_labels:
          continue
      k.append(l[0])
      k.append(m[0])
      k.append(int(m[1]))
      k.append(int(m[2]))
      k.append(l[2])
      nums.append(k)
      k = []
    if nums == []:
        return []
    lists = sorted(nums, key=itemgetter(2))
    l = handel_rest(lists)
    fo = open(p, "w")
    for i in l:
        fo.write(i)
    fo.close()

def handel_rest(lists):
    #The list will check if there is any tag next to each other, if so It will assign B-, I- else B- , O-
    nums = lists[0][3]
    word = lists[0][1]
    pres = "B-" + lists[0][1]
    lists[0][1] = pres
    an = []
    if len(lists) == 1:
        return another(lists, an)
    for i in range(1,len(lists)):
      if lists[i][2] + 1 == nums:
        word = lists[i][1]
        if word[:2] == "I-" or word[:2] == "B-":
          lists[i][1] = word[2:]
        prev = "B-" + lists[i-1][1]
        lists[i-1][1] = prev
        pres = "I-" + lists[i][1]
        lists[i][1] = pres
      else:
        word = lists[i][1]
        pres = "B-" + lists[i][1]
        lists[i][1] = pres

      nums = lists[i][3]
      print(lists)
    return another(lists, an)

def another(lists, an):
    #convertes it back into list of list/ orginal format
    for li in lists:
      k = []
      l = li[1]+" "+str(li[2])+" "+str(li[3])
      k.append(li[0])
      k.append(l)
      k.append(li[4])
      final = "\t".join(k)
      an.append(final)
    return an

def convert_all(input_paths, output):
        count = 0
        with open(input_paths) as paths:
            #reading the path of each file
            paths   = [p.strip() for p in paths]
            for p in paths:
                    # print(p)
                count = count + 1
                converter(p)


if __name__ == '__main__':
    parser = ArgumentParser(description="CoreNLP NER to IOB tags converter")
    parser.add_argument("--in", help="""Input file, each line contains comma separated *.txt,*.ann\n
    To create the input file, follow these instructuions:
    $ ls $PWD/*.txt > 1.list
    $ ls $PWD/*.ann > 2.list
    $ paste  -d "," 1.list  2.list  > input.list""", required=True)
    parser.add_argument("--out", help="""Output file""", required=False)
    args = vars(parser.parse_args())
    convert_all(args['in'], args['out'])

