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
    # можете добавить свои рецепты ;)
}


# ----  Вариант без создания шаблона -------


def dishes(request, choose):
    try:
        total_persons = int(request.GET['servings'])
    except:
        total_persons = 1

# короткий путь - servings = int(request.GET.get('servings', '1'))

    for key, value in DATA.items():
        if key == choose:
            for key_food, total in value.items():
                food = key_food
                total_food = total * total_persons
    return HttpResponse(f'Вы выбрали блюдо {choose} для готовки Вам необходимо: {food} В количестве: {total_food}')


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
