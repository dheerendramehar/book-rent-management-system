#!groovy​

// HOST_PROVISION -> server to run ansible based on provision/inventory.ini
final HOST_PROVISION = params.HOST_PROVISION

stage('Deploy') {
    node {
        
            // install galaxy roles
            sh "ansible-galaxy install -vvv -r provision/requirements.yml"        

            ansiblePlaybook colorized: true, 
            limit: "${HOST_PROVISION}",
            installation: 'ansible',
            inventory: 'provision/inventory.ini', 
            playbook: 'provision/playbook.yml', 
            sudo: true,
            sudoUser: 'dheerendra'

            //credentialsId: 'ssh-jenkins',
        
    }
}
