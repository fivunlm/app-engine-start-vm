# app-engine-start-vm
Use App Engine to start a Compute Engine VM

## Instruction

1. You have to manually create the VM instance before.
2. After VM is started, you can press the `STOP` button to stop the VM.
3. Install the packages with `pip install -r requirements.txt -t lib`.
  a.) Note if you're on macOs doing this with brew, you will need to follow this workaround listed [here](https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27#vendoring)
  b.) Second note, you'll be installing the packages locally and directly uploading them to GCP. You don't have any "install" during the deploy.
4. Deploy the app with command `gcloud app deploy app.yaml cron.yaml --version THE_VERSION` or `appcfg.py update app.yaml`.
5. Visit `/vm/start` to start the VM. Or visit the GCP console AppEngine Dashboard, which can show you errors and help you debug if needed.


