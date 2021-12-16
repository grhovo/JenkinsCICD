pipeline {
    agent { label 'docker' }
    
    environment {
        imagename = 'webpytestbdg'
	Dockerhub = '8421a05e-b878-4533-9fab-9b5356c61c41'
    }

    stages {
        stage('Checkout code from git') {
            steps {
                //git config
                git 'https://github.com/grhovo/JenkinsCICD.git'
            }
        }
        stage('Build docker image'){
            steps {
                script 
                {
                    dockerImage = docker.build imagename
                }
            }
        }
        stage('Push image to Dockerhub repo'){
            steps {
                script
                {
                    docker.withRegistry( registry, Dockerhub ) {
                    dockerImage.push("$BUILD_NUMBER")
                    dockerImage.push('latest')
                    }
                }
        }
    }
    }
}
