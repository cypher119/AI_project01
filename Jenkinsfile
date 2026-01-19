pipeline {
    agent {
        node {
            lable 'docker-agent-python'
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Start Building..'
                sh '''
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