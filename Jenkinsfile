pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                sh 'pytest -v test_movies_df.py'
            }
        }
    }
}