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
        stage('Complete') {
            steps {
                bat "echo complete!"
            }
        }     
    }
}