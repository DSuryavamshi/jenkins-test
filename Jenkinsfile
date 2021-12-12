pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                bat "conda activate jenkinstest"
                bat "pytest -v test_movies_df.py"
            }
        }
    }
}