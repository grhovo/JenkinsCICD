pipeline {
    agent { label 'docker' }
    
    environment {
	Dockerhub = '8421a05e-b878-4533-9fab-9b5356c61c41'
	registry  = 'grhovo/webpytestbdg'
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
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Push image to Dockerhub repo'){
            steps {
                script
                {
                    docker.withRegistry('',  Dockerhub ) {
                    dockerImage.push()
                    }
                }
        }
    }
        stage('Deploy to Dev environment'){
            steps {
              sh "docker run -p 8081:80 -d $registry:$BUILD_NUMBER"
        }
    }
        stage('Deploy to Prod environment'){
            steps {
              input 'Go to prod'
        }
    }
        stage('Deploy to Prod environment'){
	    agent  { label 'prod' }
            steps {
              sh "docker run -p 8081:80 -d $registry:$BUILD_NUMBER"
        }
    }
    }
}
