pipeline {
    agent { docker "python:3.6"}
    environment {
        PYPI_TOKEN = credentials('pypi-flaskrr-token')
    }
    stages {
        stage("Test") {
            steps{
                sh 'pip install -i https://mirrors.aliyun.com/pypi/simple/ tox'
                sh 'tox'
            }
            post {
                success {
                    echo 'I succeeeded!'
                    junit 'junit-report.xml'
                    archiveArtifacts 'dist/*'
                }
            }
            post {
                                always {
                    echo 'Clean up workspace.'
                    deleteDir() /* clean up our workspace */
                }
            }
        }
        stage("Upload2Pypi") {
            steps {
                sh 'tox package'
            }
            post {
                success {
                    sh 'pip install -i https://mirrors.aliyun.com/pypi/simple/ twine'
                    sh 'twine upload --skip-existing -u __token__ -p $PYPI_TOKEN'
                }
            }
        }
    }
}