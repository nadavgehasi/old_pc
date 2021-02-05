from django.db import models
from .utils import get_from_graphite


class Team(models.Model):
    name = models.CharField(max_length=255)
    info = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class System(models.Model):
    class UniverseChoice(models.TextChoices):
        IP = 'IP'
        BADID = 'Badid'

    name = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    universe = models.CharField(max_length=255, choices=UniverseChoice.choices, default=UniverseChoice.IP)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='systems')

    def __str__(self):
        return self.name


class Server(models.Model):
    class BaseChoice(models.TextChoices):
        YARKON = 'Yarkon'
        MIFKADA = 'Mifkada'

    class StatusChoice(models.TextChoices):
        UP = 'Up'
        DOWN = 'Down'

    class TagChoice(models.TextChoices):
        OPERATIONAL = 'Operational'
        TESTS = 'Tests'

    name = models.CharField(max_length=255)
    base = models.CharField(max_length=255, choices=BaseChoice.choices, default=BaseChoice.YARKON)
    status = models.CharField(max_length=255, choices=StatusChoice.choices, default=StatusChoice.UP)
    tag = models.CharField(max_length=255, choices=TagChoice.choices, default=TagChoice.OPERATIONAL)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='servers')
    systems = models.ManyToManyField(System, related_name='servers')

    @property
    def cpu_cores(self):
        return get_from_graphite(self.name, 'cpu')

    @property
    def memory_total(self):
        return get_from_graphite(self.name, 'memory.total')

    @property
    def memory_used(self):
        return get_from_graphite(self.name, 'memory.used')

    @property
    def memory_percent(self):
        return get_from_graphite(self.name, 'memory.percent')

    def __str__(self):
        return self.name
