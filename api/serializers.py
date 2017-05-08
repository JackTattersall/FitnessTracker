from rest_framework import serializers
from exercises.models.exercise import Exercise, Session
from exercises.models.workout import Workout, WorkoutExercise


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('created', 'reps', 'weight', 'sets')


class ExerciseSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=False, required=False)

    class Meta:
        model = Exercise
        fields = ('name', 'sessions')

    def create(self, validated_data):
        session_data = validated_data.pop('sessions')
        exercise = Exercise.objects.create(**validated_data)
        for session_data in session_data:
            Session.objects.create(exercise=exercise, **session_data)
        return exercise


class WorkoutSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, required=False)
    created = serializers.DateTimeField(required=False)

    class Meta:
        model = Workout
        fields = ('id', 'created', 'workout_type', 'exercises', 'name')

    def create(self, validated_data):
        exercise_data = validated_data.pop('exercises')

        tij = validated_data['name']

        workout, created = Workout.objects.get_or_create(
            name=validated_data['name'],
            defaults={
                'workout_type_id': 1
            }
        )
        for exercise_data in exercise_data:
            exercise = Exercise.objects.create(**exercise_data)
            WorkoutExercise.objects.create(exercise=exercise, workout=workout)
        return workout


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(many=False)
    workout = WorkoutSerializer(many=False)

    class Meta:
        model = WorkoutExercise
        fields = ('exercise', 'workout')
