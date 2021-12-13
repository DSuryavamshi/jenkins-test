pipeline {
    agent any

    stages {
        stage('Testing the csv file') {
            steps {                
                bat "git checkout master"
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
        stage('Push new changes') {
            steps {
                bat "git config user.name \"Jenkins User\""
                bat "git config user.email \"jenkins@system.com\""
                bat "git add ."
                bat "git commit -m \"Jenkins Changes\""
                bat "git push"
            }
        }
        // stage('Complete') {
        //     steps {
        //         bat "echo complete!"
        //         bat "dir"
        //     }
        // }     
    }
}