pipeline {
    agent any
    stages {
        stage("Clone Git Repository") {
            steps {
                git(
                    url: "https://github.com/Timuuurkaa/Administrirovanieis.git",
                    branch: "main",
                    changelog: true,
                    poll: true
                )
            }
        }
        stage("Build and test") {
            steps {
                sh "pip3 install peewee pytest"
		sh "ls"
		sh "git clone https://github.com/Timuuurkaa/Administrirovanieis.git"
		sh "python3 -m pytest Administrirovanieis/тест1.py"
            }
        }
    }
}
