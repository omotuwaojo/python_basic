book ={
    'title': 'atomic habits',
    'author': 'james clear',
    'isbn' : '234-23-2-523',
    'page_count': 234
}
# access
book_title = book['title']
book['title'] = '2020 whqt went wrong'
#keys 
keys = book.keys()
#print(keys)

#list of dict
personalities =[{
 "name":"chancelor",
 "age":18
},{
    "name":"ronald",
    "age":22
}]
#print(personalities)
bag = {
    "books": [{
         'title': 'atomic habits',
    'author': 'james clear',
    'isbn' : '234-23-2-523',
    'page_count': 234
    },{
         'title': 'c habits',
    'author': ' clear',
    'isbn' : '234-23-2-523',
    'page_count': 2345
    }],
    "stationaries": [{
        'name': "pencil",
        "quantity": 2
    }],
    'size':15,
    "color":"blue"
}
print(bag)
keys = bag.keys()
print(keys)
