pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                bat "pytest -v test_movies_df.py"
            }
        }
    }
}