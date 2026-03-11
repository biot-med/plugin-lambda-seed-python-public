def AWS_REGION = 'us-east-1'

pipeline {
    agent { label 'python' }

    stages {
        stage('Get Git Info'){
            steps {
                script {
                    currentBuild.displayName = "#${BUILD_ID}-${env.GIT_COMMIT.take(7)}"
                    COMMIT_INFO = sh(returnStdout: true, script: """
                        git log -n 1 --format=full '${env.GIT_COMMIT}' | sed -r 's/^/                        /'
                    """).trim()
                    echo """
                        build cause: ${currentBuild.buildCauses[0].shortDescription}
                        ${COMMIT_INFO}
                    """
                }
            }
        }        
        stage('deploy python'){
            steps {
                script {
                    sh """#!/bin/bash
                       apt-get update && apt install -y python3.11-venv --fix-missing
                       ln -sf /usr/bin/python3 /usr/bin/python
                       python -V
                       python -m venv seedenv
                       source seedenv/bin/activate
                       pip3 install -r requirements.txt
                       python scripts/pack.py
                       ls -la
                    """
                    GETVERSION = sh(returnStdout: true, script: """
                        grep "__version__ =" __version__.py | awk '{print \$3}' | tr -d "\\'"
                    """).trim()
                    ZIPNAME = sh(returnStdout: true, script: """
                        printf 'seed_py_${GETVERSION}.zip' 
                    """).trim()
                }
            }
        }
        stage('upload zip'){
            steps {
                script {
                    sh """
                    mkdir -p ~/.aws/
                    """
                    withAWS(credentials: 'biot', region: AWS_REGION){
                        sh """
                            mv plugin.zip ${ZIPNAME}
                            aws s3 cp '${ZIPNAME}' s3://biot-plugin-seed/ --region us-east-1
                        """
                    }
                }
            }
        }        
        stage('Git Tag'){
            when {
                branch 'master'
            }
            environment {
                GIT = credentials('github-pat') 
            }
            steps {
                sh """
                    export PROJECT_VERSION='${GETVERSION}'
                    CURRENT_TAG=\$(
                        git describe --abbrev=0 --always --tags
                    )
                    if [ \${CURRENT_TAG} != \${PROJECT_VERSION} ]; then
                        set -x
                        git config --global credential.helper store
                        {
                            echo url=\$(git config --get remote.origin.url)
                            echo "username=\$GIT_USR"
                            echo "password=\$GIT_PSW"
                        } | git credential-store store
                        set +x
                        
                        git tag "\${PROJECT_VERSION}"
                        git push origin --tags
                    fi
                """
            }
        }
    }    
    post {
        aborted {
            slackSend (color: 'gray', message: "ABORTED: job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
        failure {
            slackSend (color: 'bad', message: "FAIL: job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
        success {
            slackSend (color: 'good', message: "DONE: job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
    }    
}