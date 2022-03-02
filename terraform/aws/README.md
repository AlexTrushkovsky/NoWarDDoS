Terraform code, that spin up instances in AWS cloud, and start **NoWarDDoS** app in **docker-compose**

1) [install terraform](https://www.terraform.io/downloads)

2) update **variables.tf** (update ssh key with existing one, or create new)

3) update number of containers in:
```
./files/user_data.sh
```

(it starts 10 container by default, but you can change it, depending on instance type)

4) export AWS credentials
```
export AWS_PROFILE=$your_account_name
```

or

```
export AWS_ACCESS_KEY_ID=changeit
export AWS_SECRET_ACCESS_KEY=changeit
export AWS_DEFAULT_REGION=changeit
```


5) start instances
```
terraform init
terraform apply
```
