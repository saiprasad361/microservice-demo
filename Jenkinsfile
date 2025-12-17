pipeline {
  agent any

  environment {
    REGISTRY = "docker.io/saiprasad361"
  }

  stages {

    stage('Build Backend Image') {
      steps {
        sh 'podman build -t $REGISTRY/backend:latest backend'
      }
    }

    stage('Build Frontend Image') {
      steps {
        sh 'podman build -t $REGISTRY/frontend:latest frontend'
      }
    }

    stage('Push Images to Docker Hub') {
      steps {
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-creds',
          usernameVariable: 'REG_USER',
          passwordVariable: 'REG_PASS'
        )]) {
          sh '''
            echo $REG_PASS | podman login docker.io -u $REG_USER --password-stdin
            podman push $REGISTRY/backend:latest
            podman push $REGISTRY/frontend:latest
          '''
        }
      }
    }

    stage('Deploy to RKE2') {
      steps {
        sh 'kubectl apply -f backend/deployment.yaml'
        sh 'kubectl apply -f frontend/deployment.yaml'
        sh 'kubectl apply -f k8s/'
      }
    }
  }
}
