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

Because the frontend is static and the backend is a serverless function, local execution is easiest using Vercel CLI:

```bash
npm install -g vercel
vercel dev
```

If you do not have Vercel CLI installed, you can still preview the static frontend with a local HTTP server, but the API endpoint will run only in Vercel's environment.

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
