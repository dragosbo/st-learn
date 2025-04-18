# Time Series Visualizer - Cloud Deployment Guide

This repository contains a simple Streamlit application that visualizes time series data with interactive controls. This guide explains how to deploy this app for free using multiple cloud services, with step-by-step instructions for each method.

## Application Overview

The application generates synthetic time series data with configurable trend, seasonality, and noise components. Users can:
- Adjust the time series parameters using sliders
- View the raw data and interactive visualizations
- Apply rolling averages with configurable window sizes
- Download the generated data as CSV

## Deployment Options

### 1. Streamlit Community Cloud (Recommended)

**Pros:**
- Specifically designed for Streamlit apps
- Direct GitHub integration
- No configuration needed for public sharing
- Free tier is generous for personal projects

**Cons:**
- Only works with Streamlit apps
- Public repositories only (unless on paid plan)

**Deployment Steps:**

1. Push your code to a public GitHub repository with the following structure:
   ```
   repository/
   ├── time_series_app.py
   └── requirements.txt
   ```

2. Visit [Streamlit Community Cloud](https://streamlit.io/cloud)

3. Sign in with your GitHub account

4. Click "New app" and select your repository, branch, and the main Python file:
   - Repository: your-username/your-repo
   - Branch: main
   - Main file path: time_series_app.py

5. Click "Deploy"

Your app will be available at `https://your-username-your-repo-main-xxxxx.streamlit.app`

### 2. GitHub Codespaces/Dev Containers

**Pros:**
- Works with any Python web framework
- Integrated with GitHub
- 60 hours free per month
- Full development environment

**Cons:**
- More suited for development than production
- URLs change each session
- Limited runtime

**Deployment Steps:**

1. Add a `.devcontainer` folder to your repository with the following files:

   `devcontainer.json`:
   ```json
   {
     "name": "Python Streamlit",
     "image": "mcr.microsoft.com/devcontainers/python:3.11",
     "forwardPorts": [8501],
     "postCreateCommand": "pip install -r requirements.txt",
     "customizations": {
       "vscode": {
         "extensions": ["ms-python.python"]
       }
     }
   }
   ```

2. Push to GitHub

3. Open your repository in GitHub and click "Code" > "Open with Codespaces"

4. Once your environment loads, run:
   ```bash
   streamlit run time_series_app.py
   ```

5. Click the "Open in Browser" button when the notification appears

### 3. Render

**Pros:**
- Supports various Python web frameworks
- Easy deployment process
- Free SSL certificates
- Persistent URLs

**Cons:**
- Free tier services spin down after 15 minutes of inactivity
- Limited to 750 hours per month

**Deployment Steps:**

1. Create a `render.yaml` file:
   ```yaml
   services:
     - type: web
       name: streamlit-time-series
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: streamlit run time_series_app.py --server.port $PORT --server.address 0.0.0.0
       envVars:
         - key: PYTHON_VERSION
           value: 3.9.0
   ```

2. Create an account on [Render](https://render.com)

3. Connect your GitHub account

4. Create a new "Web Service" and select your repository

5. Render will detect the configuration and deploy automatically

### 4. Google Colab with Streamlit

**Pros:**
- Free with Google account
- No setup required
- Access to GPU/TPU resources

**Cons:**
- Sessions timeout after inactivity
- Not designed for production deployment
- URLs change each session

**Deployment Steps:**

1. Create a new Colab notebook

2. Add and run the following cells:

   ```python
   # Install dependencies
   !pip install streamlit pandas numpy plotly pyngrok
   ```

   ```python
   # Write the app code to a file
   %%writefile app.py
   
   # Paste your time_series_app.py content here
   ```

   ```python
   # Run the app with pyngrok
   from pyngrok import ngrok
   
   !streamlit run app.py &>/dev/null&
   
   # Create a tunnel
   public_url = ngrok.connect(8501)
   print(f"Streamlit app is running at: {public_url}")
   ```

3. Follow the public URL displayed to access your app

### 5. Railway

**Pros:**
- User-friendly interface
- GitHub integration
- 500 hours of free compute per month
- $5 monthly credit for free tier

**Cons:**
- Credit card required for verification
- Limited resources

**Deployment Steps:**

1. Create a `Procfile` in your repository:
   ```
   web: streamlit run time_series_app.py --server.port $PORT --server.address 0.0.0.0
   ```

2. Sign up at [Railway](https://railway.app)

3. Create a new project and select "Deploy from GitHub repo"

4. Connect your GitHub account and select your repository

5. Railway will automatically detect and deploy your app

### 6. Fly.io

**Pros:**
- Generous free tier (3 shared-cpu-1x 256mb VMs)
- Global edge deployment
- Persistent volumes available
- Docker-based deployment

**Cons:**
- Requires Docker knowledge
- More complex setup

**Deployment Steps:**

1. Create a `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   
   COPY . .
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "time_series_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. Install the [Fly CLI](https://fly.io/docs/hands-on/install-flyctl/)

3. Run `flyctl auth login` and sign up

4. Run `flyctl launch` in your project directory

5. Deploy with `flyctl deploy`

## Recommendation

For Streamlit applications, **Streamlit Community Cloud** is the most straightforward option with the best developer experience. Simply connect your GitHub repository, and your app is deployed instantly with a public URL.

## Local Development

To run this app locally:

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run time_series_app.py`
4. Open your browser at `http://localhost:8501`

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python Documentation](https://plotly.com/python/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
