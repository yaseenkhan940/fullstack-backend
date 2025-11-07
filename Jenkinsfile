pipeline {
  agent any

  stages {
    // no explicit git step — Jenkins already checked out the repo
    stage('Set up Python Environment') {
      steps {
        echo '🐍 Setting up virtual environment...'
        sh '''
          python3 -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run FastAPI') {
      steps {
        echo '🚀 Starting FastAPI application (background)...'
        sh '''
          . venv/bin/activate
          # start uvicorn in background, save PID to file, redirect logs
          nohup venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port 8000 > app.log 2>&1 &
          echo $! > app.pid
          echo "uvicorn started, PID=$(cat app.pid)"
        '''
      }
    }
  }

  post {
    success { echo '✅ Deployment Successful! FastAPI should be running.' }
    failure { echo '❌ Build failed. Check console output for details.' }
  }
}
