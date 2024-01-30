
from diagrams import Diagram, Cluster

from diagrams.aws.management import Organizations, OrganizationsAccount, OrganizationsOrganizationalUnit
from diagrams.aws.general import Users, User

with Diagram("SSO-State", show=False, direction="TB"):
    gg = Users("Group")
    uu= User("User")

    with Cluster('Groups'):

        gg_0= Users("AWSLogArchiveVie\nwers")

        with Cluster("AWSControlTowerAdmins"):

                gg_1= [User("velez94@protonma\nil.com"),]

        gg_2= Users("AWSSecurityAudit\nors")

        with Cluster("SecOps_Adms"):

                gg_3= [User("w.alejovl+secops\n-labs@gmail.com"),]

        gg_4= Users("AWSServiceCatalo\ngAdmins")

        with Cluster("AWSAccountFactory"):

                gg_5= [User("velez94@protonma\nil.com"),]

        gg_6= Users("AWSSecurityAudit\nPowerUsers")

        gg_7= Users("AWSLogArchiveAdm\nins")

        with Cluster("DevSecOps_Admins"):

                gg_8= [User("DevSecOpsAdm"),]
