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

## Hosting on the web

This repository contains a `build/web` folder (a static web build produced by tools like `pygbag`) that can be hosted as a static site. I added a GitHub Actions workflow (`.github/workflows/deploy-pages.yml`) that will deploy the contents of `build/web` to GitHub Pages whenever you push to `main`.

Quick options to host the project:

- GitHub Pages (recommended for this repo): push your `build/web` to the repository and the workflow will publish it at `https://<your-username>.github.io/<repo>/`.
- Netlify or Vercel: connect the repository and set the publish directory to `build/web`.
- Render / Railway: create a static site service and point it to `build/web`.

If you prefer to host a Flask backend (e.g., `app.py` / dynamic server): consider Render, Railway, or Fly.io. That requires a WSGI server (Gunicorn) and a `requirements.txt`.

If you'd like, I can:

- Commit a `requirements.txt` and `Procfile` for deploying a Flask server.
- Add a small GitHub Actions workflow to build the project before deploy (if you need build steps).
- Configure a DNS/CNAME or create a one-click deploy button for Netlify.

## Automatic Heroku deploy (GitHub Actions)

You can deploy the Flask-based site to Heroku automatically on push to `main` using the workflow added at `.github/workflows/deploy-heroku.yml`.

Badge (shows latest workflow status):

```markdown
[![Heroku Deploy](https://github.com/issim9825/tree-game/actions/workflows/deploy-heroku.yml/badge.svg?branch=main)](https://github.com/issim9825/tree-game/actions/workflows/deploy-heroku.yml)
```

Required repository secrets (Settings → Secrets → Actions):

- `HEROKU_API_KEY` — your Heroku account API key (Account settings → API Key).
- `HEROKU_APP_NAME` — the exact name of your Heroku app (e.g., `my-tree-game`).
- `HEROKU_EMAIL` — the email address associated with your Heroku account.

How to add the secrets:

1. Open your GitHub repo page → Settings → Secrets and variables → Actions.
2. Click "New repository secret" and add each secret name and value above.

Once the secrets are set, push to `main` and the `deploy-heroku` workflow will run and attempt to deploy your app to the Heroku app named in `HEROKU_APP_NAME`.

Troubleshooting:

- If the workflow fails with authentication errors, double-check that `HEROKU_API_KEY` is correct and has deploy access.
- If the Heroku slug is too large because `build/web` contains many binary assets, consider using container deploy (`heroku container:push`) or trimming large files from the repo.
