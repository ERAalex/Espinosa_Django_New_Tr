from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'drunk_hamster': {
        'хомяк, потолще': 1,
        'вино, мл': 1,
        'виски, мл': 1,
        'водка, мл, повышаем градус': 1,
    },
}


# ----  Вариант без создания шаблона -------


def dishes(request, choose):
    try:
        total_persons = int(request.GET['servings'])
    except:
        total_persons = 1

# короткий путь - servings = int(request.GET.get('servings', '1'))

    list_f = []
    full_text = ''
    for key, value in DATA.items():
        if key == choose:
            count = 0
            for key_food, total in value.items():
                count += 1                                        # нужен для красивого вывода, каждый пункт будет  1)   2)   3)
                count_str = '|' + str(count) + ').  '
                total_f_int = round((total * total_persons),2)    # отбросим после запятой числа (а то выдает много)
                total_f_str = str(total_f_int)
                list_f += count_str + key_food + ' в количестве: ' + total_f_str + '  .'

            full_text += ''.join(list_f)     # собираем все в 1 строку для красивого и удобного вывода


    return HttpResponse(f'Вы выбрали блюдо {choose} для готовки Вам необходимо: \n {full_text}')


def index(request):
   return render(request, 'calculator/index.html')








# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
