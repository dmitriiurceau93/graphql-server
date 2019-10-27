import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from django_graphql_movies.movies.models import Actor, Movie

# Create a Graphql type for the actor model
class ActorType(DjangoObjectType):
    class Meta:
        model = Actor

# Create a Graphql type for the movie model
class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

# Create a Query type
class Query(ObjectType):
    actor = graphene.Field(ActorType, id=graphene.Int())
    movie = graphene.Field(MovieType, id=graphene.Int())
    actors = graphene.Field(ActorType)
    movies = graphene.Field(MovieType)

    def resolve_actor(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Actor.objects.get(pk=id)
        
        return None

    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Movie.objects.get(pk=id)
        
        return None

    def resolve_actors(self, info, **kwargs):
        return Actor.object.all()

    def resolve_movies(self, info, **kwargs):
        return Movie.object.all()
    