data = {}
maxnamelen = 0
with open(".txt", "r", encoding = "utf-8") as f:
    while True:
        try:
            name, group, *tag = f.readline().split()
            data[name] = {}
            data[name]["name"] = name
            data[name]["group"] = group
            data[name]["tag"] = tag
            maxnamelen = max(len(name), maxnamelen)
        except:
            break

def search(keywords):
    keywords = list(set(keywords))
    numKey = len(keywords)
    l = [[] for _ in range(numKey + 1)]
    for name in data:
        cnt = 0
        for keyword in keywords:
            if "#" + keyword in data[name]["tag"]:
                cnt += 1
        l[cnt].append(data[name].values())
    for i in range(numKey, - 1, - 1):
        if len(l[i]) > 0:
            if i == numKey:
                print("all keywords matched (100 %):")
            elif i == 0:
                continue
            else:
                print(f"{i} of {numKey} keywords matched ({i*100//numKey} %):")
            for name, group, tag in l[i]:
                print(f"name: {name: <{maxnamelen+2}}  ", end = "")
                print(f"group: {group}  ", end = "")
                print(f"tag: {', '.join(tag)}")
        print("")

with open("keyword.txt", "r") as f:
    kwd = f.readline().split()
search(kwd)

                
    