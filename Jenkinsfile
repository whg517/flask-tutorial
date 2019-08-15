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
        }
        stage("Upload2Pypi") {
            steps {
                sh 'tox -e package'
            }
            post {
                success {
                    sh 'pip install -i https://mirrors.aliyun.com/pypi/simple/ twine'
                    sh 'twine upload --repository-url https://test.pypi.org/legacy/ --skip-existing -u __token__ -p $PYPI_TOKEN dist/*'
                }
            }
        }
    }
}