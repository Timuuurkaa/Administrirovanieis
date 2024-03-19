pipeline {
    stages {
        stage('Build') {
            steps {
                 sh '''#!/bin/bash
                         pip3 install peewee pytest && python3 -m pytest тест1.py
                 '''
            }
        }
    }
}
