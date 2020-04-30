# VideoAnalytics_Mediaserver
Mediaserver instance template code for a [ultimately censored] app - just another bit of trash on Github
### Контроллер медиасервера
#### Функции
1.	Приём запросов клиента на выдачу потоков / записей с камер;
2.	Получение и передача клиенту потока, выданного сервером аналитики по ID, предоставленному диспетчером;
3.	Управление размерами области, используемой для позиционирования видеоизображения в окне браузера;
4.	Установление физических характеристик выходного потока, требуемых для  передачи трафика по протоколу HLS. 

Рис. 1. Схема установления доступа к видеофрагменту (записи) через медиасервер.
<p align="center">
  <img src="https://user-images.githubusercontent.com/55311053/80411729-f5658b00-88cc-11ea-8c4f-24e5620ddf5e.jpg" />
</p>
<br/>
<em>Пояснения к визуализации</em>
<ol>
<li>Пользователь выбирает интересующую запись из списка доступных для просмотра в своём аккаунте и подтверждает воспроизведение;</li>
<li>HTTP-запрос GET передаётся на медиасервер и принимается к выполнению;</li>
<li>Медиасервер использует идентификатор записи для поиска в специализированной БД;</li>
<li>Сервер БД определяет релевантную запись и возвращает связанный с ней набор фреймов потока в ответ на запрос;</li>
<li>Медиасервер реализует настройку протокольной совместимости данных и направляет результирующий поток в виде ответа клиенту;</li>
<li>Полученные на терминале данные последовательно воспроизводятся в диалоговом окне приложения.</li>
</ol>  

Рис. 2. Схема определения базовых классов (not match, but tribute to UML class diagram).<br/>
![allegedClasses (2)](https://user-images.githubusercontent.com/55311053/80410118-58a1ee00-88ca-11ea-870e-07491dda0dd3.jpg)
<br/><br/>

Рис. 3. Схема определения программных интерфейсов.<br/>
![controller_db](https://user-images.githubusercontent.com/55311053/80387445-f1277680-88a8-11ea-8e96-ada1f01def62.jpg)

Таблица 1. Состав и назначение функций API контроллера.
| Функция | Назначение|
|---|---|
| handleHTTPRequest | приём в работу GET-запроса с идентификатором выбранной камеры |
| requestServerAssigned | отправка запроса диспетчеру для определения ассоциированного сервера аналитики |
| requestLiveStreaming | отправка запроса на выдачу потока сервером аналитики |
| findRecordById | получение записи из БД по известному ID |
| findRecordsByCamId | возврат данных о всех записях, ассоциированных с конкретной камерой |
| findRecordsByInterval | возврат данных о всех записях видео с конкретной камеры, полученных в рамках заданного интервала времени |
| transcode | установление HLS-совместимости выходного потока |
| resize | управление размером области, выделенной под воспроизведение видеоданных в окне клиентского браузера |
<p></p>
<strong>Проработка технологического стека</strong> 
<ul>
  <li>Язык разработки: Python 3.7</li>
  <li>Фреймворк адаптированной веб-разработки: Flask 1.1.2</li>
  <li>Библиотека функций обработки и анализа видео: OpenCV 3</li>
  <li>СУБД: PostgreSQL 12</li>
</ul>  
<br/>
Факторы оптимальности текущей структуры стека:<br/>
<ul>
  <li>универсальная модульная поддержка элементов OpenCV в Python/Flask;</li>
  <li>минимальные временные издержки для настройки OpenCV в Python/Flask;</li> 
  <li>удобство, доступность представления справочной информации и высокая скорость разработки на Python;</li> 
  <li>практичность структуры проекта и высокая динамика развёртывания сервисов веб-приложений в Flask;</li>
  <li>широкий набор тематически идентичных проектов на Python для форсированного освоения актуальных технологий;</li>
  <li>высокая производительность обработки SQL-запросов в PostgreSQL, в т.ч. в условиях интенсивного конкурентного проведения CRUD-транзакций;</li> 
  <li>практичность и гибкость конфигурирования БД в PostgreSQL (особо отмечаются визуальное и утилитарное исполнение интерфейса администрирования pgAdmin).</li>
</ul>  
