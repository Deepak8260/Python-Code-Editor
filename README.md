# Python Code Editor Web App

A serverless Python code editor designed for direct deployment on Vercel.

## Project Overview

This repository now contains a static frontend and a Vercel-compatible Python API endpoint. Users can write Python code in the browser, submit it to the `/api/run` function, and view the output immediately.

## Files and Structure

- `index.html` - Static frontend served by Vercel
- `static/style.css` - Styling for the editor interface
- `api/run.py` - Vercel serverless Python API endpoint
- `requirements.txt` - Runtime dependencies for the serverless API
- `vercel.json` - Vercel build and route configuration

## Requirements

- Python 3.x runtime provided by Vercel
- No additional external Python packages are required for the API endpoint

## Running Locally

This project is easiest to run locally with the Vercel CLI because the backend is a serverless API function.

1. Install Vercel CLI if you do not already have it:

```bash
npm install -g vercel
```

2. From the project root, start the local Vercel development server:

```bash
vercel dev
```

3. Open the URL shown in the terminal, usually:

```bash
http://127.0.0.1:3000
```

4. In the browser, use the editor and click Run. The `/api/run` endpoint is served locally by Vercel.

### Notes

- You do not need to install any Python dependencies manually for this app.
- If you want to run only the static frontend without the backend, you can open `index.html` directly in a browser, but `/api/run` will not work outside Vercel development.

## Deployment on Vercel

1. Install Vercel CLI or use the Vercel dashboard.
2. From the project root, deploy with:

```bash
vercel
```

The static app will be served from `index.html`, and code execution requests will be handled by `api/run.py`.

## How It Works

- The browser sends code and optional stdin to `/api/run`
- The serverless function executes the submitted Python code with a 10-second timeout
- Standard output or error output is returned as JSON and displayed in the UI

## Security Note

This demo executes arbitrary Python code on the server. Running untrusted code can be dangerous and should only be done in isolated environments.
