git add .
git commit -m "update server"
git push origin ibrahim_current

git checkout deployment
git merge ibrahim_current -m "merged with ibrahim_current"
git push origin deployment

ssh developer@192.168.1.2 -p 2929 "cd /webapps/mhealth/mhealth_web_portal/;git add .;git commit -m "stash"; git pull origin deployment;sudo supervisorctl restart mhealth;"

git checkout ibrahim_current


