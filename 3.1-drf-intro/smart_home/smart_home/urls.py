
from django.contrib import admin
from django.urls import path, include
from measurement.views import See_and_Create_All_Api, Count_Update_Delete, Meas_Create


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api_all', See_and_Create_All_Api.as_view()),  # Создать счетчик + вывести все счетчики, Краткая инфа


    path('api/<int:pk>', Count_Update_Delete.as_view()),   # изменение, удаление счетчика + полная инфа по счетчику


    # MEASER

    path('mes_create', Meas_Create.as_view()),  # Создать температуру, задать ID

    # path('mes_up_del/<int:pk>', Meas_Update_Delete.as_view()),  # mes_temperature_изменение, удаление счетчика
    #


]

#Обратите внимание на параметр pk URL-адреса. <int:pk>
# Это имя, которое используется по умолчанию и фреймворком Django и Django REST для извлечения записи с id равным pk.
# Поэтому изначально, если нигде ничего не переопределено, то следует в маршруте прописывать именно это имя параметра.
# Далее, оно автоматически будет выделено из URL-запроса и прочитана соответствующая запись из таблицы БД.
# Фреймворк эти действия делает на автомате.

# http://127.0.0.1:8000/api/1     внимание! не ставь / т.к его нет в path выще. т.е не пиши  ..../api/1/


