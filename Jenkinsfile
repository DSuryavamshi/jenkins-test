pipeline {
    agent any
    def cmd_exec(command) {
        return bat(returnStdout: true, script: "${command}").trim()
    }

    stages {
        stage('Test') {
            steps {
                cmd_exec(sh 'pytest -v test_movies_df.py')
            }
        }
    }
}