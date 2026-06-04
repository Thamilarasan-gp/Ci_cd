pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                bat 'echo Building Website...'
            }
        }

        stage('Test') {
            steps {
                bat '''
                if exist index.html (
                    echo Test Passed
                ) else (
                    exit 1
                )
                '''
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                xcopy /E /Y * C:\\website\\
                '''
            }
        }
    }
}