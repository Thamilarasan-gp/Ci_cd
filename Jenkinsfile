pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Thamilarasan-gp/Ci_cd.git'
            }
        }

        stage('Test') {
            steps {
                bat '''
                if exist index.html (
                    echo Website Found
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