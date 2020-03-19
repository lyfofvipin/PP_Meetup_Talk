pipeline{
    agent{
        node "master"
    }

    parameters{
        string( name: "Users", defaultValue: "user1,user2,vipin3699" )
        string( name: "passwords", defaultValue: "passwd1,passwd2" )
    }

    stages{
        stage("Clone the Repo"){
            steps{
                git 'https://github.com/vipin3699/PP_Meetup_Talk.git'
            }
        }
        stage("Run Test"){
            steps{
                withCredentials([string(credentialsId: 'fb', variable: 'pass')]) {
                    sh "python login_fb.py $Users $passwords,$pass"
                }
            }
        }
    }
}
