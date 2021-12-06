#!/usr/bin/env python

from azure_sas_upload import upload_using_sas
# SAS URL
sas_url_for_upload = "Add SAS URL here"
# File to upload
file_to_upload = "logo.png"

# Start upload
r= upload_using_sas(sas_url_for_upload, file_to_upload)
# Print upload status . 201 is success.
print ("Upload Status :" + str(r))