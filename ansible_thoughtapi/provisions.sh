ansible-galaxy install jdauphant.nginx
ansible-playbook -i plugins/inventory/ provision_ec2.yml
ansible-playbook -i plugins/inventory/ --private-key=/mnt/1e396172-74e1-4592-b9ca-2a106c768fc1/codefellows/aws/keypair1.pem deploy_django.yml -vvvvvv
