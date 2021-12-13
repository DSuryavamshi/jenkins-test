pipeline {
    agent any

    stages {
        stage('Testing the csv file') {
            steps {                
                bat "pytest -v test_movies_df.py"
            }
        }
        stage('Testing the process python code') {
            steps {                
                bat "pytest -v test_process_movies_data.py"
            }
        }
        stage('Processing the movies csv') {
            steps {
                bat "python process_movies_data.py"
            }
        }
        stage('Testing the processed csv') {
            steps {
                bat "pytest -v test_processed_movies_csv.py"
            }
        }
        stage('Complete') {
            steps {
                bat "echo complete!!"
            }
        }     
    }
}