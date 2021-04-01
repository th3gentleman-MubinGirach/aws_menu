import os
import time

os.system("tput setaf 6")
print('Lets create a High Availability Architecture using AWS cli \n')


def instanceA():
    print("Using ami-0bcf5425cdc1d8a85")
    os.system("tput setaf 5")
    print("listing your subnets")
    os.system("aws ec2 describe-subnets | grep SubnetId")
    time.sleep(5)
    os.system("tput setaf 2")
    subnet = input("Enter the subnet id:   ")

    print("listing your security groups")
    os.system("aws ec2 describe-security-groups | grep GroupId")
   
    sg = input("Enter the security group:  ")
    number = input("Enter the number of instances you want to launch: ")
    keyname = "aws ec2 describe-key-pairs | grep KeyName"
    os.system(keyname)
    keypair = input("Enter the key pair name you want to use for launching the instance: ")
    launch = "aws ec2 run-instances --image-id ami-0bcf5425cdc1d8a85" + " " + "--count " + number + " " + "--instance-type t2.micro --key-name " + keypair + " " + "--security-group-ids " + sg + " --subnet-id " + subnet + " " + "| grep  InstanceId"
    os.system(launch)


def instanceR():
    print("Using ami-0a9d27a9f4f5c0efc")
    os.system("tput setaf 4")
    print("listing your subnets")
    os.system("aws ec2 describe-subnets | grep SubnetId")
    
    os.system("tput setaf 2")
    subnet = input("Enter the subnet id:   ")
    os.system("tput setaf 4")
    print("listing your security groups")
    os.system("aws ec2 describe-security-groups | grep GroupId")
   
    sg = input("Enter the security group:  ")
    os.system("tput setaf 2")
    number = input("Enter the number of instances you want to launch: ")
    os.system("tput setaf 4")
    print("lsiting the available key pairs")
    os.system("aws ec2 describe-key-pairs | grep KeyName")
    os.system("tput setaf 2")
    keypair = input("Enter the key pair name you want to use for launching the instance: ")
    launch = "aws ec2 run-instances --image-id ami-0a9d27a9f4f5c0efc" + " " + "--count " + number + " " + "--instance-type t2.micro --key-name " + keypair + " " + "--security-group-ids " + sg + " --subnet-id " + subnet + " " + "| grep  InstanceId"
    os.system(launch)


def ebs():
    os.system("tput setaf 2")
    size = input("Enter the size without the keyword gb: ")
    region = input("which region : ")
    ebsc = "aws ec2 create-volume --volume-type gp2 --size " + size + " --availability-zone " + region
    os.system(ebsc)


def s3():
    os.system("tput setaf 2")
    names3 = input("Enter the name of s3 bucket you would like to create: ")
    regionse = input("Enter the region: ")
    s3create = "aws s3api create-bucket --bucket " +names3+" --region "+regionse
    os.system(s3create)


def upload():
    os.system("tput setaf 2")
    fl = input("Path of the file to be uploaded eg /root/folder/file.jpg:  ")
    os.system("aws s3api  list-buckets | grep Name ")
    os.system("tput setaf 2")
    bucket = input("Name of the bucket where it needs to be uploaded: ")
    upld = "aws s3 cp " + fl + " " + "s3://" + bucket + "/"
    os.system(upld)
    public = input("Should i create cdn for the same: ")
    if public == "yes":
        nmfl = input("Tell me the name of the file: ")
        mkpblc = "aws s3api put-object-acl --bucket " + bucket + " --key" + " " + nmfl + " " + "--acl public-read "
        #print(mkpblc)
        os.system(mkpblc)
        regionsel = input("The region where the bucket is created: ")

        cdn = "aws cloudfront create-distribution --origin-domain-name " + bucket + ".s3." + regionsel + ".amazonaws.com --default-root-object " + nmfl + " " + "| grep DomainName "
        os.system(cdn)
        print("You can use the above cloudfront domain name for your image")


    else:
        print("as you wish")


def attach():
    os.system("aws ec2 describe-volumes | grep VolumeId ")
    os.system("tput setaf 2")
    vlmid = input("Enter the volume id you want to attach: ")
    os.system("aws ec2 describe-instances | grep InstanceId")
    instance = input("Enter the instance id: ")
    attaching = "aws ec2 attach-volume --volume-id " + vlmid + " --instance-id " + instance + " --device /dev/sdf"
    os.system(attaching)


def key():
    name = input("What should be the name of the key: ")
    print("OK let me create a key into your /root/ directory")
    finalkey = 'aws ec2 create-key-pair --key-name' + ' ' + name + ' ' + '--query "KeyMaterial"' + ' ' + '--output text >' + name + '.pem'
    os.system(finalkey)
    print("done")


def mnt():
    os.system("mkfs.ext4 /dev/xvdf")
    os.system("yum install httpd")
    os.system("mount /dev/xvdf /var/www/html")


def connect():
    keyinput = input("What is the name of the keypair you want to use eg keypair.pem: ")
    chmod = "sudo chmod 400" + " " + keyinput
    os.system(chmod)
    os.system("tput setaf 4")
    print("listing the IP of your running instances")
    os.system("aws ec2 describe-instances | grep PublicIpAddress ")
    ip = input("Enter the IP address of your instance: ")
    connecttoec2 = "ssh -i" + " " + keyinput + " " + "ec2-user@" + ip
    os.system(connecttoec2)

def html():
	print("Use the cloudfront domain name for the content in HTML ")
	print("########################################################")
	fileopen = open("index.html", "w")
	cntnthtml=input("Please enter the content you want in html file:   ")
	fileopen.writelines(cntnthtml)
	fileopen.close()

	


def linux():
    while True: 
        print('Below is the Menu just for you choose an appropriate option \n')
        os.system("tput setaf 2")
        print('AWS menu by th3gentleman..Mubin Girach')
        os.system('tput setaf 4')
        print('----------------------------------------')
        os.system('tput setaf 3')
        print('To Configure AWS- Press C \n'
              'To create key pair- Press K \n'
              'To launch EC2 instance- Press E \n'
              'To create EBS volume- Press V \n'
	      'To attach EBS volume to your instance-Press A \n'
              'To create s3 bucket - Press s3 \n'
              'To upload object on S3 bucket and make a cdn for it- Press O \n'
	      'To connect to your instance -Press CN	\n'
	      'To create a html file -Press HTML \n'
              'To mount the EBS storage to /var/www/html- Press MNT \n'
              'To copy the html file into your /var/www/html -Press CP \n'
              'To exit from this program -Press X \n')
        os.system("tput setaf 4")
        print('---------------------------------------------------------')
        os.system('tput setaf 3')
        menu = input("Enter your input: ")

        if menu == "C":
            os.system("aws configure")
        elif menu == "K":
            key()
	
        elif menu == "E":
            print('This is the list of os we have you can select anything from this')
            print('---------------------------------------------------------------')
            ami = input('For Amazon Linux -Press A \n'
                        'For Red hat linux - Press R \n')
            if ami == "A":
                instanceA()
            elif ami == "R":
                instanceR()
	
	  
        elif menu == "V":
            ebs()
        elif menu == "s3":
            s3()
        elif menu == "O":
            upload()
        elif menu == "A":
            attach()
        elif menu == "X":
            break
            
        elif menu == "MNT":
            mnt()
        elif menu == "CN":
            connect()
        elif menu == "CP":
            copy=input("Enter the directory of your file eg /root/index.html: ")
            copypaste="sudo cp"+" "+copy+" "+"/var/www/html"
            os.system(copypaste)
        elif menu == "HTML":
            html()
	


linux()                               









