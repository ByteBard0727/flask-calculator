pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'my-flask-calculator'
        DOCKER_REGISTRY = 'docker.io'
        REPO_NAME = 'ByteBard0727/my-flask-calculator'
        // I have added the dir in the mounted volume of my containerized jenkins
        PATH = "/var/jenkins_home/docker:$PATH"  // please note if you run this on your own pc this directory might be different
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone repository
                git 'https://github.com/ByteBard0727/flask-calculator.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE}:latest")
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests inside the Docker container
                    docker.image("${DOCKER_IMAGE}:latest").inside {
                        sh 'pytest test_app.py'
                    }
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    docker.withRegistry("https://${DOCKER_REGISTRY}", 'dockerhub-credentials') {
                        docker.image("${DOCKER_IMAGE}:latest").push('latest')
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the Docker image (e.g., run it on a server)
                // For example, use Docker commands to deploy
                sh 'docker run -d -p 5000:5000 ${DOCKER_IMAGE}:latest'
            }
        }
    }

    post {
        always {
            // Clean up
            cleanWs()
        }
    }
}