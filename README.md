# app-engine-start-vm
Use App Engine to start a Compute Engine VM

## Instruction

1. You have to manually create the VM instance before.
2. After VM is started, you can press the `STOP` button to stop the VM.
3. Install the packages with `pip install -r requirements.txt -t lib`.
4. Deploy the app with command `gcloud app deploy app.yaml cron.yaml --version THE_VERSION` or `appcfg.py update app.yaml`.
5. Visit `/vm/start` to start the VM.
