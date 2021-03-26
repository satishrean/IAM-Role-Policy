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
          sh '''
          sudo apt-get update
          sudo apt-get install python3-pip
          python3 -m pip3 install --user boto3
          python3 role.py
          '''
        }
      }
    }
  }
