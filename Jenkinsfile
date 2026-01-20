pipeline {
    agent {
        label 'docker-agent-alpine'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Start Building..'
                sh '''
                python3 -m venv .venv
                ./.venv/bin/activate
                pip install -r requirements.txt
                python3 main.py
                python3 main.py circle --radius=1
                python3 main.py rectangle --height=2 --base=3
                python3 main.py triangle --height=2 --base=3
                '''
                echo 'End of build'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}