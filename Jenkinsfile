pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Building the project..."
                sh 'echo Build step executed'
            }
        }
        stage('Test') {
            steps {
                echo "Running tests..."
                sh 'echo Tests executed'
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploy step..."
                sh 'echo Deploy simulated'
            }
        }
    }
}
