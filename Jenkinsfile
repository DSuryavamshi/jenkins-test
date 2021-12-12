pipeline {
    agent any

    stages {
        stage('Testing the csv file') {
            steps {
                bat "pytest -v test_movies_df.py"
            }
        }
        stage('Processing the movies csv') {
            steps {
                bat "python process_movies_data.py"
            }
        }
        stage('Testing the processed csv') {
            steps {
                bat "pytest -v test_processed_movies_data.py"
            }
        }
        stage('Pushinh the new file to the repository') {
            steps {
                bat "git config --global user.email \"system@jenkins.com\""
                bat "git config --global user.name \"Jenkins User\""
                bat "git add ."
                bat "git commit -m \"Jenkins changes\""
                bat "git push origin master"
            }
        }
        
    }
}