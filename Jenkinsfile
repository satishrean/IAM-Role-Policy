String credentialsId = 'awsCredentials'
stage('checkout') {
    node {
      cleanWs()
      checkout scm
    }
  }
stage('create role') {
    node {
      withCredentials([[
        $class: 'AmazonWebServicesCredentialsBinding',
        credentialsId: credentialsId,
        accessKeyVariable: 'AWS_ACCESS_KEY_ID',
        secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
      ]]) {
        ansiColor('xterm') {
          sh 'python3 role.py'
        }
      }
    }
  }
