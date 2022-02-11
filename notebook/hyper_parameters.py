def get_hyper_paras():
    user_id = "opentlc-mgr"
    PROJECT_NAME = "CustomerChurn-opentlc-mgr"
    EXPERIMENT_NAME = "CustomerChurn-opentlc-mgr"
    experiment_name = "customerchurn-opentlc-mgr"
    minioFilename="part-00000-aa888b5b-fd89-431e-831f-cfd9d79e4548-c000.csv"
    s3BucketFullPath = "full_data_csv"+user_id+"/"+minioFilename
    
    return user_id,PROJECT_NAME,EXPERIMENT_NAME,experiment_name,s3BucketFullPath
