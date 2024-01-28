import os
import boto3
from speaksynk_flow_processor.SpeakSynkFlowProcessor import SpeakSynkFlowProcessor
from speaksynk_flow_processor.utils.utils import createFolder, get_file_path
from speaksynk_flow_processor.constants.constants import (
    WORKING_DIR,
    S3_BUCKET_NAME,
    INPUT_FOLDER_NAME,
    OUTPUT_FOLDER_NAME,
    DYNAMO_DB_TABLE_NAME
)

class AWSSpeakSynkFlowProcesor(SpeakSynkFlowProcessor):
    def __init__(self):
        super().__init__()
        self.s3 = boto3.client("s3")
        self.dynamodb = boto3.client('dynamodb') 
        self.bucket_name = os.environ[S3_BUCKET_NAME]
        self.input_folder = os.environ[INPUT_FOLDER_NAME]
        self.output_folder = os.environ[OUTPUT_FOLDER_NAME]
        self.tableName = os.environ[DYNAMO_DB_TABLE_NAME]

    def download(self, filekey):
        super().download(filekey)
        filePath = os.path.join(WORKING_DIR, filekey)
        createFolder(os.path.dirname(filePath))
        self._logger.debug("Video path: %s, Video Key: %s" % (filePath, filekey))
        self._logger.debug(self.s3)
        self.s3.download_file(self.bucket_name, filekey, filePath)
        self._logger.debug("File created")

    def upload(self, filekey, fileName):
        super().upload(filekey, fileName)
        filePath = get_file_path(fileName)
        self._logger.debug("Uploading video: %s" % filePath)
        with open(filePath, "rb") as out_handle:
            self._logger.debug("Uploading video to: %s" % filekey)
            self.s3.upload_fileobj(out_handle, self.bucket_name, filekey)
            self._logger.info("Finished uploaded video")
    
    def check_file(self, filekey):
        try:
            meta_data = self.s3.head_object(Bucket=self.bucket_name, Key=filekey)
            return True, meta_data
        except self.s3.exceptions.NoSuchKey as e:
            return False, None
        except self.s3.exceptions.ClientError as e:
            return False, None
    
    def uploadStats(self):
        super().uploadStats()
        self.dynamodb.put_item(TableName=self.tableName, Item=self.getTrackData())