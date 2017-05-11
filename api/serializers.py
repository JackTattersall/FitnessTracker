from rest_framework import serializers
from exercises.models.exercise import Exercise, Session, ExerciseSession
from exercises.models.workout import Workout, WorkoutExercise, WorkoutType
import datetime


class ExerciseSerializer(serializers.ModelSerializer):
    sessions = serializers.SerializerMethodField()

    def get_sessions(self, obj):
        sessions = Session.objects.filter(exercises__pk=obj.id)
        if sessions:
            print('vincent')
            session = sessions.latest('created')
            if session.completed:
                return {
                        "reps": session.reps,
                        "sets": session.sets,
                        "weight": session.weight
                }
            else:
                return 0
        else:
            return 0

    class Meta:
        model = Exercise
        fields = ('name', 'sessions', 'workouts')

    def create(self, validated_data):
        session_data = validated_data.pop('sessions', None)
        exercise = Exercise.objects.create(**validated_data)
        if session_data:
            for session_data in session_data:
                Session.objects.create(exercise=exercise, **session_data)
        return exercise


class SessionSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(required=False)
    exercises = ExerciseSerializer(many=True, required=False)

    class Meta:
        model = Session
        fields = ('created', 'reps', 'weight', 'sets', 'exercises', 'completed')

    def create(self, validated_data):
        exercise_data = validated_data.pop('exercises', None)
        session = Session.objects.create(**validated_data)

        if exercise_data:
            for exercise_data in exercise_data:
                exercise = Exercise.objects.get(
                    name=exercise_data['name']
                )
                ExerciseSession.objects.create(session=session, exercise=exercise)

        return session


class WorkoutTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutType
        fields = ('name', 'description')


class WorkoutSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, required=False)
    created = serializers.DateTimeField(required=False)
    completed = serializers.DateTimeField(required=False)
    workout_type = WorkoutTypeSerializer(required=False)

    class Meta:
        model = Workout
        fields = ('id', 'created', 'workout_type', 'exercises', 'completed', 'is_complete')

    def create(self, validated_data):
        exercise_data = validated_data.pop('exercises', None)
        workout_type_data = validated_data.pop('workout_type', None)
        is_complete_data = validated_data.pop('is_complete', None)

        if workout_type_data:
            workout_type = WorkoutType.objects.create(**workout_type_data)
            workout = Workout.objects.create(workout_type_id=workout_type.id)
        else:
            workout_created = validated_data['created']
            workout = Workout.objects.get(created=workout_created)

        if exercise_data:
            for exercise_data in exercise_data:
                exercise = Exercise.objects.create(**exercise_data)
                WorkoutExercise.objects.create(exercise=exercise, workout=workout)

        if is_complete_data:
            workout_created = validated_data['created']
            workout_completed = datetime.datetime.now()
            workout = Workout.objects.filter(created=workout_created).update(completed=workout_completed,
                                                                             is_complete=True)

        return workout


class WorkoutExerciseSerializer(serializers.ModelSerializer):
    exercise = ExerciseSerializer(many=False)
    workout = WorkoutSerializer(many=False)

    class Meta:
        model = WorkoutExercise
        fields = ('exercise', 'workout')
