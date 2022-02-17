"""
Overenginering 101.

I want to be flexible in the connection with the outside world
    FastAPI makes heavy use of dependencies, so we could make 
    a factory function with takes the config as Dependency, which 
    determines if we want a PostgresRepo or a InMemoryRepo.

    Not entirely sure how this going to help me ...
"""
