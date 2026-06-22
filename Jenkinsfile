pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Pulling latest code from GitHub...'
                git branch: 'main', url: 'https://github.com/AmanZandah/student-registration-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Creating virtual environment and installing packages...'
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Verifying the Flask app imports without errors...'
                bat 'venv\\Scripts\\python.exe -c "import app"'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded: code pulled, dependencies installed, app verified.'
        }
        failure {
            echo 'Pipeline failed: check the console output above for the error.'
        }
    }
}
