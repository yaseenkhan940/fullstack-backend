pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📦 Cloning repository...'
                git branch: 'main', credentialsId: 'github-creds', url: 'https://github.com/yaseenkhan940/fullstack-backend.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                echo '🐍 Setting up virtual environment...'
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run FastAPI') {
            steps {
                echo '🚀 Starting FastAPI application...'
                bat '''
                call venv\\Scripts\\activate
                start /B uvicorn main:app --host 0.0.0.0 --port 8000
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful! FastAPI is running at http://127.0.0.1:8000'
        }
        failure {
            echo '❌ Build failed. Check console output for details.'
        }
    }
}
