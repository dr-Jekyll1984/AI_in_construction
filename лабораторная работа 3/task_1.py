# TODO Напишите функцию для поиска индекса товара

list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
def index(list, item):
    try:
        return list.index(item)
    except ValueError:
        return None
for find_item in ['банан', 'груша', 'персик']:
    index_item = index(list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
