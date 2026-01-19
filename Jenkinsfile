pipeline {
    agent {
        label 'docker-agent-alpine'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Start Building..'
                echo 'still building'
                echo 'End of build'
                '''
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