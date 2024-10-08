from django.db import models


class Place(models.Model):
    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

    name = models.CharField("Название", max_length=255)

    coordinates = models.CharField("Координаты", max_length=255)

    text_riddle = models.TextField("Загадка при прибытии на место", blank=True, null=True)

    video_riddle_url = models.URLField("Видео загадка")
    video_story_url = models.URLField("Видео с историей места")

    task_file = models.FileField("Задание", upload_to='tasks/')

    def __str__(self) -> str:
        return str(self.name)


class Region(models.Model):
    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")

    def __str__(self):
        return str(self.name)


class Path(models.Model):
    class Meta:
        verbose_name = "Траектория"
        verbose_name_plural = "Траектории"

    name = models.CharField("Название", max_length=255)
    places = models.ManyToManyField(Place, verbose_name="Места", through='PlaceInPath')
    region = models.ForeignKey(Region, verbose_name="Регион", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class PlaceInPath(models.Model):
    class Meta:
        verbose_name = "Место в траектории"
        verbose_name_plural = "Места в траектории"
        ordering = ['position']
        unique_together = ('place', 'path')

    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место")
    path = models.ForeignKey(Path, on_delete=models.CASCADE, verbose_name="Траектория")
    position = models.PositiveIntegerField("Позиция")

    def __str__(self):
        return f"Место '{self.place.name}'. Траектория '{self.path.name}'. Позиция {self.position}"


class Team(models.Model):
    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

    name = models.CharField("Название", max_length=255)
    contacts = models.TextField("Контакты для связи", max_length=255)
    path = models.ForeignKey(Path, on_delete=models.CASCADE, verbose_name="Выбранная траектория")

    def __str__(self):
        return str(self.name)


class TeamPlaceAnswer(models.Model):
    class Meta:
        verbose_name = "Ответы команды"
        verbose_name_plural = "Ответы команд"

    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Команда")
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место")

    start_datetime = models.DateTimeField("Время начала отгадывания места", blank=True, null=True)
    end_datetime = models.DateTimeField("Время окончания отгадывания места", blank=True, null=True)

    photo = models.ImageField("Фото-подтверждение", upload_to='photos/', blank=True, null=True)
    task_answer = models.TextField("Ответ на задание", blank=True, null=True)

    def __str__(self):
        return f"{self.team.name}: {self.place.name}"
