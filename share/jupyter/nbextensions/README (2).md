
# Getting Started

### Clone the repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/calculator_pro.git
cd calculator_pro
```

### Build and Run the Application in Docker
Once you have Docker installed and cloned the repository, follow these steps to run the calculator app:

1. **Build the Docker image**:
   ```bash
   docker-compose up --build
   ```

2. **Access the app**:
   Open your browser and go to `http://localhost:8050` or `http://127.0.0.1:8050` to access the app.

3. **Stop the app**:
   When you're done, you can stop the app by running:
   ```bash
   docker-compose down
   ```

## Running the App Locally (Without Docker)
If you prefer to run the app locally without Docker, you can follow these steps:

1. **Set up a Python virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scriptsctivate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   python calculator.py
   ```

4. **Access the app**:
   Go to `http://localhost:8050` or `http://127.0.0.1:8050` in your browser to see the app.

## Files

### `calculator.py`
This is the main application file. It defines the layout of the calculator, including buttons for numbers and operations, and the logic for handling user input and performing calculations.

### `Dockerfile`
The `Dockerfile` contains instructions for building the Docker image. It installs the necessary dependencies, copies the app into the Docker container, and runs the app using Python.

### `docker-compose.yml`
The `docker-compose.yml` file defines the services required to run the app, builds the Docker container, and maps the container's port `8050` to the host machine.

### `requirements.txt`
This file lists the dependencies required for the project (e.g., Dash). When Docker builds the image, it installs the dependencies listed here.

## Acknowledgments
- [Dash by Plotly](https://dash.plotly.com/) - A Python framework for building web applications.
