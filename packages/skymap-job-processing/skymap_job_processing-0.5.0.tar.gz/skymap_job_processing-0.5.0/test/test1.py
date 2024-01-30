from skymap_job_processing.processing import Credential, JobConfig, KeyValuePair, Processor
import boto3
import os
if __name__ == "__main__":
    credential = Credential(
        endpoint="https://smzmn4uxvn2mplksckvqxn22ki0dalut.lambda-url.ap-southeast-1.on.aws",
        secret_key="sk_797a7693186b0C22873BBc097396B5bBB7b4eE53",
        region="ap-southeast-1",
        ws_endpoint="wss://ppkp6aeky4.execute-api.ap-southeast-1.amazonaws.com/dev"
    )
    bucket_name = "machine-learning-task"
    input_prefix="farmboundary-bayer/input/"
    output_prefix="farmboundary-bayer/output/"
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=input_prefix, Delimiter='/')
    input_objects = filter(lambda obj: obj["Size"] != 0, map(lambda obj: {**obj, "Name": os.path.basename(obj['Key']).replace(".tif","")}, response.get('Contents', [])))
    input_objects = list(map(lambda obj: {**obj, "Index": int(obj["Name"].split("_")[-1])}, input_objects))
    input_objects = sorted(input_objects, key=lambda obj: obj["Index"])

    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=output_prefix, Delimiter='/')
    output_objects = list(map(lambda obj: {**obj, "Name": os.path.basename(obj['Prefix'][0:-1])}, response.get('CommonPrefixes', [])))
    output_objects = list(map(lambda obj: {**obj, "Index": int(obj["Name"].split("_")[-1])}, output_objects))
    output_objects = sorted(output_objects, key=lambda obj: obj["Index"])
    output_ids = [obj["Index"] for obj in output_objects]
    incompleted_objects = [obj for obj in input_objects if obj["Index"] not in output_ids]

    print(len(incompleted_objects))
    for obj in incompleted_objects:
        name = obj['Name']
        main_job = JobConfig(
            definition ="FarmBoundaryJobDef",
            queue_name = "MachineLearningProdGpuSpotJobQueue",
            environment = [
                KeyValuePair("INPUT_PATH",f"/data/farmboundary-bayer/input/{name}.tif"),
                KeyValuePair("OUTPUT_PATH",f"/data/farmboundary-bayer/output/{name}")
            ]
        )
        processor = Processor(
            credential=credential,
            name= name,
            main_job=main_job,
            is_persistent_storage=False,
        )
        processor.run(wait=False)
        print("Submitted:", name)