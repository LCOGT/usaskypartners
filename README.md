# USA Sky Partners

Website for the USA Sky Partners project written in Django, Wagtail and Wagtail localize

### Get snapshot of live site:

```
kubectl exec -it <pod-name> -n prod -c backend -- python manage.py dumpdata -e wagtailcore.groupcollectionpermission -e sessions -e admin -e wagtailsearch --natural-foreign --natural-primary | gzip > fullsite.json.gz
```

Read data into local sandbox with:
```
./manage.py migrate; ./manage.py remove_demo_page; ./manage.py loaddata fullsite.json.gz
```
