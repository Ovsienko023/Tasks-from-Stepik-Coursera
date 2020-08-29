from collections import deque


graph = {"you": ["Bob", "Alisa", "Kler"], 
        "Alisa" : ["Peggi"], 
        "Kler" : ["Markm"],
        "Bob" : ['Kop']}


def is_mango(human):
    if human[-1] == 'm':
        return True
    return False


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = list()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_mango(person):
                return True
            else:
                try:
                    search_queue += graph[person]
                except KeyError:
                    continue
                searched.append(person)
    return False

print(search('Alisa'))
