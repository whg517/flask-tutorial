pipeline {
    agent { docker "python:3.6"}
    stages {
        stage("Test") {
            steps{
                sh 'pip install -i https://mirrors.aliyun.com/pypi/simple/ tox'
                sh 'tox'
            }
            post {
                success {
                    junit 'junit-report.xml' 
                }
            }
        }

    }
}