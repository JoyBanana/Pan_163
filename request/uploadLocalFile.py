import os
from request.initKEY import getClient

file_name = "ding.py"  # 待上传文件的名称

bucket = "joybanana"
client = getClient()


result = client.create_multipart_upload(bucket, file_name)
# 分块上传ID用于后续分块上传操作
upload_id = result["response"].find("UploadId").text

# step 2. 上传分块
index = 0
slice_size = 100 * 1024 * 1024
with open(os.path.join(os.getcwd(), file_name), "rb") as fp:
    while True:
        index += 1
        part = fp.read(slice_size)
        if not part:
            break
        client.upload_part(bucket, file_name, index, upload_id, part)

# step 3. 列出所有分块，完成分块上传
rParts = client.list_parts(bucket, file_name, upload_id)
Parts = rParts["response"]
partETags = []
for k in Parts.findall("Part"):
    partETags.append({"part_num": k.find("PartNumber").text, "etag": k.find("ETag").text})

client.complete_multipart_upload(bucket, file_name, upload_id, partETags)
