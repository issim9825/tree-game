# Small Python-based game

This project is to learn how to use the pygame module.

## My thoughts on pygame

Works fine to make mini-games,  
would rather use a Game Engine  
like Unity or Unreal Engine for large-scale games

## Upcoming features

- Sell threes
- Buy items
- character selection
- levels
- etc..


Troubleshooting:

- If the workflow fails with authentication errors, double-check that `HEROKU_API_KEY` is correct and has deploy access.
- If the Heroku slug is too large because `build/web` contains many binary assets, consider using container deploy (`heroku container:push`) or trimming large files from the repo.
