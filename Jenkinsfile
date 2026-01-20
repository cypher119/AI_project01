pipeline {
    agent {
        label 'docker-agent-alpine'
    }
    stages {
        stage('Build') {
            steps {
                echo 'Start Building..'
                radius=1
                height=2
                base=3
                pip install -r requirements.txt
                python3 main.py
                python3 main.py circle --radius=1
                python3 main.py rectraingle --height=2 --base=3
                python3 main.py rectraingle --heignt=2 --base=3
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