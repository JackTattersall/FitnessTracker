from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    sessions = models.ManyToManyField(u'Session', through=u'ExerciseSession', related_name=u'exercises')

    class Meta:
        db_table = 'FITNESS_exercise'

    def __str__(self):
        return self.name


class Session(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    reps = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    sets = models.IntegerField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'FITNESS_session'

    def __str__(self):
        return str('reps = {} sets = {} weight = {}'.format(self.reps, self.weight, self.sets))


class ExerciseSession(models.Model):
    session = models.ForeignKey(Session)
    exercise = models.ForeignKey(Exercise)

    class Meta:
        db_table = 'FITNESS_exercise_sessions'


