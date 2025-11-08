pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo '📦 Cloning repository...'
                git branch: 'main', url: 'https://github.com/yaseenkhan940/fullstack-backend.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                echo '🐍 Setting up virtual environment...'
                sh '''
                    set -e
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run FastAPI') {
            steps {
                echo '🚀 Starting FastAPI app...'
                sh '''
                    set -e
                    cd "$WORKSPACE"
                    . venv/bin/activate
                    pkill -f uvicorn || true
                    nohup venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 > uvicorn.log 2>&1 &
                    sleep 3
                    curl -fS http://127.0.0.1:8000/ || (cat uvicorn.log && exit 1)
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful! FastAPI is running on port 8000.'
        }
        failure {
            echo '❌ Build failed. Check console output for details.'
        }
    }
}
