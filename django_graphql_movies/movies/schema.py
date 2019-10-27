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

    