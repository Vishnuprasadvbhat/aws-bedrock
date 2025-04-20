# Amazon Bedrock Series

## Overview
This project leverages **AWS Bedrock** Large Language Models (LLMs) for AI-driven applications. The setup process ensures a seamless environment for interaction with AWS services.

## Initial Setup
To begin, use any IDE of your preference. This guide uses **VSCode**.

## 1. Create a Virtual Environment
A virtual environment is recommended to maintain dependencies separately.

Run the following commands in the terminal:
For macOS/Linux users, activate the virtual environment using:
``` bash
source venv/bin/activate 
```


For Windows users, activate the virtual environment using:
```bash
python -m venv venv
cd venv/Scripts
activate.ps1  # For PowerShell users
``` 
## 2. Creating a Git Repository
Create a new repository on GitHub or any other platform of your choice.

  #### Errors I faced during repo creation due to previous git initializations
  ```(venv) PS D:\AWS\Bedrock> git remote add origin https://github.com/Vishnuprasadvbhat/aws-bedrock.git                        
  fatal: detected dubious ownership in repository at 'D:/'
  'D:/' is owned by:
          'S-1-5-18'
  but the current user is:
          'S-1-5-21-520853544-919835508-2353064755-1001'
  To add an exception for this directory, call:

          git config --global --add safe.directory D:/
  ```
#### Solution By Git 

  `git config --global --add safe.directory D:/`

### Initializing Git Repository

#### **Reason:** 
I realized the issue was simply that I forgot to initialize Git. 😅 

#### **Steps Taken**
1. **Initialize Git** in the project directory:
   ```bash
   git init

Here’s your updated documentation snippet with the Git initialization step:
### Initializing Git Repository

#### **Reason:** 
I realized the issue was simply that I forgot to initialize Git. 😅 

#### **Steps Taken**

1. **Initialize Git** in the project directory:
  ``` bash
  git init 
  ```

2. **Check for existing remote repositories:**
  ``` bash
  git remote -v
  ```

3.  **Add the remote origin using your repository URL:**

 ``` bash
  git remote add origin <repo-url>
  ```

4. **Verify that the remote origin is set correctly:**
```bash 
git remote -v
```

## **Another blunder:**
I already had a main branch with gitignore file etc, in my terminal i accidently push it to a non-existing branch master, leading to its creation. now I dont want that. 

### **I want to undo it**

We can do that using `git revert`

  Using `git revert` will create a new commit that undoes the changes made in the previous commit.

  you just need to pass the old commit's hashcode to `git revert` command. you can get the hashcode using `git log` command. or previous push log eg: `4b0f231`. 
  
### **Now the commit it reverted, but what about the branch?**
  You need to delete the branch, cause it will create trouble in the future.

  Just use `git push origin --delete <branch-name>` to delete the branch from remote repository.

### **Issue Still Exists**

Once i have deleted it, I tried pushing it to the `main` branch but I got this `fatal: refusing to merge unrelated histories` 

This happens when the local repository and remote repository have different histories, often when the repository was initialized separately. Due to creation of two branches and pushes to the new branch, the old one became outdated. 

So we `git fetch origin main` to update the local repository with the latest changes from the remote repository. Then we can use `git rebase origin/main` to rebase our local branch onto the remote branch. 

Then i got this `Successfully rebased and updated refs/heads/main` 

The issue is now resolved. I can push my changes to the remote repository using cmd `git push origin main`

This worked for me!!!... I hope it works for you too!!!

## 3. Install Required Packages following essential packages are used:
- boto3 – AWS SDK for Python, enabling interaction with AWS services like S3 and EC2.
- awscli – AWS Command Line Interface, allowing users to interact with AWS via command-line.

Installing via requirements.txt
It is best practice to install dependencies using a requirements.txt file.

Create the file
``` bash
echo > requirements.txt 
```
Add the module names inside `requirements.txt`:

```bash 
boto3
awscli
```
Now install the dependencies:
```bash
pip install -r requirements.txt
```

Verification
After installation, confirm package availability
``` bash
pip list | grep "boto3\|awscli"
```

## 4. Now Let's Configure AWS CLI:

Creating a User in IAM (AWS)
1. Navigate to IAM
- Sign in to the AWS Management Console.
- In the Services menu, go to IAM (Identity and Access Management).

2. Create a New User
- Click on Users in the left-hand menu.
- Select Add user.
- Enter the username as: testadmin.
- Under Access type, select AWS Management Console access (for console login) or Programmatic access (for API/CLI usage), depending on requirements.
- Click Next: Permissions.

3. Attach Administrative Permissions
- Under Set permissions, choose Attach existing policies directly.
- Search for and attach the policy AdministratorAccess.
- Click Next: Tags.

4. Add a Description Tag
- In the Tag key, enter a meaningful tag such as Description.
- Set the Tag value to: testuserkey.
- Click Next: Review.

5. Review and Create User
- Ensure the user details, permissions, and tags are correct.
- Click Create user.

6. Generate Access Keys
- Once the user is created, navigate to the user’s details page.
- Click Security credentials.
- Under Access keys, click Create access key.
- Select Use case based on your needs (e.g., Command Line Interface (CLI)).
- Click Create.
- Download the .csv file containing the access key ID and secret access key.



## Things to Do:
- Download the .csv file containing the access key and secret key.
- Store it securely, either in your project folder or another safe location.


## 5. Configure AWS

To configure AWS credentials, run the following command in your **VSCode terminal**:

```bash
aws configure
```
**Required Inputs:**

You will be prompted to enter the following details:

1. AWS Access Key ID – Your unique Access Key ID.
2. AWS Secret Access Key – The corresponding Secret Access Key.
3. Default region name – Specify your AWS region (e.g., us-east-1, ap-south-1).
4. Default output format – Leave it blank or specify format (e.g., json, table, text).



