pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                bat 'if exist index.html (echo PASS) else exit 1'
            }
        }

        stage('Deploy') {
            steps {
                bat 'xcopy /E /Y * C:\\website\\'
            }
        }
    }
}